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
        self._cells = []
        i = 1
        while i < self._num_cols:
            column = []
            j = 1
            while j < self._num_rows:
                column.append(Cell(i, j, self._win))
                j += 1
            self._cells.append(column)
            i += 1
           