from solver import Solver

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
    sudoku_solver.solve()
    sudoku_solver.print_sudoku()
