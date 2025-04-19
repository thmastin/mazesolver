from cell import Cell
from point import Point

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()

    def _create_cells(self):
        matrix = []
        i = 1
        row = 0
        while i < self._num_cols + 1:
            col = 0
            column = []
            j = 1
            while j < self._num_rows + 1:
                cell = Cell(Point(i, j), Point(i, j + 1), self._win)
                column.append(cell)
                j += 1
                col += 1
            matrix.append(column)
            i += 1
            row += 1
        print("Length of Matrix: ", len(matrix))
        print("Length of Column at Index 0:", len(matrix[0])) 
        print("First Cell Top Corner: ", matrix[0][0]._x1, ",", matrix[0][0]._y1)
        print("First Cell Bottom Corner: ", matrix[0][0]._x2, ",", matrix[0][0]._y2)   
        print("Last Cell Top Corner: ", matrix[-1][-1]._x1, ",", matrix[-1][-1]._y1)
        print("Last Cell Bottom Coner: ", matrix[-1][-1]._x2, ",", matrix[-1][-1]._y2 )
        print("")   