from cell import Cell
from point import Point

import time

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
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                cell = Cell(Point(0, 0), Point(0, 0), self._win)
                column.append(cell)
            self._cells.append(column)
                
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        cell = self._cells[i][j]

        cell._x1 = x1
        cell._y1 = y1
        cell._x2 = x2
        cell._y2 = y2

        cell.draw()

        self._animate()
        
    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)