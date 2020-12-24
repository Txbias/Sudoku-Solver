class Solver:
    def __init__(self, path):
        self.sudoku = self._load_sudoku_from_file(path)

    def _load_sudoku_from_file(self, path: str) -> list:
        with open(path) as file:
            content = file.read()

        sudoku = list()
        lines = content.split('\n')

        for line in lines:
            numbers = [int(x) for x in line.split(' ')]
            sudoku.append(numbers)

        return sudoku

    def is_solved(self):
        empty = self.find_all_empty()
        return len(empty) == 0

    def find_all_empty(self):
        empty = list()
        for i in range(len(self.sudoku)):
            for j in range(len(self.sudoku[i])):
                if self.sudoku[i][j] == 0:
                    empty.append((i, j))

        return empty

    def valid(self, num, pos):
        # check row
        row = pos[0]
        for i in range(len(self.sudoku[row])):
            if self.sudoku[row][i] == num:
                return False

        # Check col
        for i in range(len(self.sudoku)):
            for j in range(len(self.sudoku[0])):
                if i == pos[1] and self.sudoku[j][i] == num:
                    return False

        # Check box
        box_x = pos[0] // 3
        box_y = pos[1] // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.sudoku[j][i] == num:
                    return False

        return True

    def print_sudoku(self):
        for i in range(len(self.sudoku)):
            if i % 3 == 0 and i != 0:
                print("-------------------------------------------")

            for j in range(len(self.sudoku[0])):
                if j % 3 == 0 and j != 0:
                    print("|", end="")

                if j == 8:
                    print(self.sudoku[i][j])
                else:
                    print(str(self.sudoku[i][j]) + " ", end="")

    def solve(self):
        empty = self.find_all_empty()
        solved = []
        tested = {}
        found = False

        while not self.is_solved():
            pos = empty[len(solved)]

            for num in range(1, 10):
                if pos not in tested:
                    tested[pos] = []
                if self.valid(num, pos) and num not in tested[pos]:
                    found = True
                    self.sudoku[pos[0]][pos[1]] = num
                    solved.append(pos)
                    tested[pos].append(num)
                    break
                elif num not in tested[pos]:
                    tested[pos].append(num)

            if not found:
                self.sudoku[pos[0]][pos[1]] = 0
                tested[pos] = []
                if len(solved) > 0:
                    last_pos = empty[len(solved) - 1]
                    self.sudoku[last_pos[0]][last_pos[1]] = 0
                    solved.remove(last_pos)
                else:
                    print("Sudoku is not solvable")
                    exit(0)

            found = False
