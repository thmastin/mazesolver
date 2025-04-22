from cell import Cell
from point import Point

import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        if seed is not None:
            self._seed = random.seed(seed)
            
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited_cells()

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
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            if i > 0 and not self._cells[i-1][j].visited:
                possible_directions.append((i - 1, j))
            if i < len(self._cells) - 1 and not self._cells[i+1][j].visited:
                possible_directions.append((i + 1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                possible_directions.append((i, j - 1))
            if j < len(self._cells[0]) - 1 and not self._cells[i][j+1].visited:
                possible_directions.append((i, j + 1))
            if possible_directions == []:
                self._draw_cell(i, j)
                return
            new_i, new_j = random.choice(possible_directions)
            if new_i < i:
                self._cells[i][j].has_left_wall = False
                self._cells[new_i][new_j].has_right_wall = False
            elif new_i > i:
                self._cells[i][j].has_right_wall = False
                self._cells[new_i][new_j].has_left_wall = False
            elif new_j < j:
                self._cells[i][j].has_top_wall = False
                self._cells[new_i][new_j].has_bottom_wall = False
            else:
                self._cells[i][j].has_bottom_wall = False
                self._cells[new_i][new_j].has_top_wall = False
            
            self._draw_cell(i, j)
            self._break_walls_r(new_i, new_j)

    def _reset_visited_cells(self):
        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._cells[i][j].visited = False

    def solve(self):
        start_cell = self._cells[0][0]
        print(f"START CELL WALLS: left={start_cell.has_left_wall}, right={start_cell.has_right_wall}, top={start_cell.has_top_wall}, bottom={start_cell.has_bottom_wall}")
        
        # Check each condition separately
        condition1 = 0 < len(self._cells[0]) - 1
        condition2 = not start_cell.has_bottom_wall
        condition3 = not self._cells[0][1].visited
        
        print(f"Condition 1 (j < len(self._cells[0]) - 1): {condition1}")
        print(f"Condition 2 (not has_bottom_wall): {condition2}")
        print(f"Condition 3 (not next cell visited): {condition3}")
        
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        print(f"Exploring cell ({i}, {j})")
        self._animate()

        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            print("Found the Exit!")
            return True
        
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            print(f"Moving left from ({i}, {j}) to ({i-1}, {j})")
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i-1][j].draw_move(self._cells[i][j], True)
        if i < len(self._cells) - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            print(f"Moving right from ({i}, {j}) to ({i+1}, {j})")
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i+1][j].draw_move(self._cells[i][j], True)
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            print(f"Moving up from ({i}, {j}) to ({i}, {j-1})")
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j-1].draw_move(self._cells[i][j], True)
        if j < len(self._cells[0]) - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            print(f"Moving down from ({i}, {j}) to ({i}, {j+1})")
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j+1].draw_move(self._cells[i][j], True)

        return False
        