from line import Line
from point import Point

class Cell:
    def __init__(self, top_point, bottom_point, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = top_point.x
        self._x2 = bottom_point.x
        self._y1 = top_point.y
        self._y2 = bottom_point.y
        self._win = win

    def draw(self, line_color="black", line_width=2):
        if self._win is None:
            return
        
        if self.has_left_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x1, self._y2)
            left_wall = Line(point_1, point_2)
            self._win.draw_line(left_wall, line_color)
        else:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x1, self._y2)
            left_wall = Line(point_1, point_2)
            self._win.draw_line(left_wall, "white")

        
        if self.has_right_wall:
            point_1 = Point(self._x2, self._y1)
            point_2 = Point(self._x2, self._y2)
            right_wall = Line(point_1, point_2)
            self._win.draw_line(right_wall, line_color)
        else:
            point_1 = Point(self._x2, self._y1)
            point_2 = Point(self._x2, self._y2)
            right_wall = Line(point_1, point_2)
            self._win.draw_line(right_wall, "white")


        if self.has_top_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x2, self._y1)
            top_wall = Line(point_1, point_2)
            self._win.draw_line(top_wall, line_color)
        else:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x2, self._y1)
            top_wall = Line(point_1, point_2)
            self._win.draw_line(top_wall, "white")


        if self.has_bottom_wall:
            point_1 = Point(self._x1, self._y2)
            point_2 = Point(self._x2, self._y2)
            bottom_wall = Line(point_1, point_2)
            self._win.draw_line(bottom_wall, line_color)
        else:
            point_1 = Point(self._x1, self._y2)
            point_2 = Point(self._x2, self._y2)
            bottom_wall = Line(point_1, point_2)
            self._win.draw_line(bottom_wall, "white")


    def draw_move(self, to_cell, undo=False):        
        path = Line(self.cell_middle(), to_cell.cell_middle())
        if undo:
            self._win.draw_line(path, "gray")
        else:
            self._win.draw_line(path, "red")
            
    
    def cell_middle(self):
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
