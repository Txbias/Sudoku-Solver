from gui import SudokuUI
import time


class Solver():
    sudoku = []

    def __init__(self, sudoku):
        self.sudoku = sudoku

    def is_solved(self):
        empty = self.find_all_empty()
        if len(empty) == 0:
            return True
        else:
            return False

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
                if i == pos[1]:
                    if self.sudoku[j][i] == num:
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

            for j in range(len(sudoku[0])):
                if j % 3 == 0 and j != 0:
                    print("|", end="")

                if j == 8:
                    print(self.sudoku[i][j])
                else:
                    print(str(self.sudoku[i][j]) + " ", end="")

    def solve(self, draw_puzzle):
        empty = self.find_all_empty()
        solved = []
        tested = {}
        found = False

        while not self.is_solved():

            pos = empty[len(solved)]

            for num in range(1, 10):
                if not pos in tested:
                    tested[pos] = []
                if self.valid(num, pos) and not num in tested[pos]:
                    found = True
                    self.sudoku[pos[0]][pos[1]] = num
                    solved.append(pos)
                    tested[pos].append(num)
                    break
                elif not num in tested[pos]:
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


if __name__ == "__main__":
    sudoku = [[6, 0, 5, 7, 0, 0, 1, 3, 2],
               [7, 0, 0, 6, 0, 0, 5, 0, 8],
               [0, 1, 9, 3, 0, 0, 0, 0, 4],
               [0, 2, 0, 0, 0, 3, 0, 0, 0],
               [0, 7, 3, 9, 0, 0, 2, 5, 0],
               [0, 5, 1, 2, 0, 0, 0, 0, 9],
               [5, 0, 8, 0, 0, 0, 0, 2, 0],
               [0, 4, 0, 0, 7, 6, 9, 1, 5],
               [0, 9, 0, 0, 4, 0, 6, 8, 0]]

    sudoku_solver = Solver(sudoku)
    sudoku_solver.solve(sudoku)
    sudoku_solver.print_sudoku()
