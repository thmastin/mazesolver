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
        i = 0
        while i < self._num_cols:
            column = []
            j = 0
            while j < self._num_rows:
                y1 = self._y1
                top_point = Point(self._x1, y1)
                y1 -= self._cell_size_y
                bottom_point = Point(self._x1, y1)
                column.append(Cell(top_point, bottom_point))
                j += 1
            self._cells.append(column)
            self._x1 += self._cell_size_x
            i += 1
           