from tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM
import threading


MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9


class SudokuUI(Frame):

    def __init__(self, solver):
        self.setup = False
        self.solver = solver
        self.parent = Tk()
        Frame.__init__(self, self.parent)

        self.row, self.col = 0, 0

        self.last_sudoku = solver.sudoku

        self.__initUI()
        self.parent.mainloop()

    def __initUI(self):
        self.parent.title("Sudoku Löser")
        self.pack(fill=BOTH)
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT)
        self.canvas.pack(fill=BOTH, side=TOP)

        solve_button = Button(self,
                              text="Sudoku lösen",
                              command=self.__solve)

        solve_button.pack(fill=BOTH, side=BOTTOM)

        self.__draw_grid()
        self.draw_puzzle()

        self.canvas.bind("<Button-1>", self.__cell_clicked)
        self.setup = True


    def __draw_grid(self):
        '''
        Draws the
        '''
        for i in range(10):
            color = "blue" if i % 3 == 0 else "gray"

            x0 = MARGIN + i * SIDE
            y0 = MARGIN
            x1 = MARGIN + i * SIDE
            y1 = HEIGHT - MARGIN
            self.canvas.create_line(x0, y0, x1, y1, fill=color)

            x0 = MARGIN
            y0 = MARGIN + i * SIDE
            x1 = WIDTH - MARGIN
            y1 = MARGIN + i * SIDE
            self.canvas.create_line(x0, y0, x1, y1, fill=color)


    def get_differences(self, sudoku1, sudoku2):
        assert len(sudoku1) == len(sudoku2)

        differences = []
        for i in range(len(sudoku1)):
            if sudoku1[i] != sudoku2[i]:
                differences.append(i)

        return differences


    def draw_puzzle(self):
        # TODO: only update numbers that are neccessary

        if self.setup:
            print(self.last_sudoku == self.solver.sudoku)
            differences = self.get_differences(self.last_sudoku, self.solver.sudoku)
            print(differences)
        else:
            differences = []
            for i in range(9):
                differences.append(i)

        self.last_sudoku = self.solver.sudoku

        for i in range(9):
            if not i in differences:
                continue
            self.canvas.delete('num' + str(i))
            for j in range(9):
                answer = self.solver.sudoku[i][j]
                if answer != 0:
                    x = MARGIN + j * SIDE + SIDE / 2
                    y = MARGIN + i * SIDE + SIDE / 2
                    color = 'black'
                    self.canvas.create_text(
                        x, y, text=answer, tags='num' + str(i), fill=color
                            )


    def __solve(self):
        threading.Thread(target=self.solver.solve, args=(self.draw_puzzle,)).start()


    def __cell_clicked(self, event):
        x, y = event.x, event.y
        if(MARGIN < x < WIDTH - MARGIN and MARGIN < y < HEIGHT - MARGIN):
            self.canvas.focus_set()

            # get row and col numbers from x, y coordinates
            row, col = (y - MARGIN) / SIDE, (x - MARGIN) / SIDE

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
    sudoku2 = [[6, 1, 5, 7, 0, 0, 1, 3, 2],
               [7, 0, 0, 6, 0, 0, 5, 0, 8],
               [0, 1, 9, 3, 0, 0, 0, 0, 4],
               [0, 2, 0, 0, 0, 3, 0, 0, 0],
               [0, 7, 3, 9, 0, 0, 2, 5, 0],
               [0, 5, 1, 2, 0, 0, 0, 0, 9],
               [5, 0, 8, 0, 0, 0, 0, 2, 0],
               [0, 4, 0, 0, 7, 6, 9, 1, 5],
               [0, 9, 9, 0, 4, 0, 6, 8, 0]]

    #print(get_differences(sudoku, sudoku2))
