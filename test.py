from solver import Solver

if __name__ == "__main__":

    sudoku_solver = Solver('example_sudoku.txt')
    sudoku_solver.solve()
    sudoku_solver.print_sudoku()
