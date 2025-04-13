from line import Line
from point import Point

class Cell:
    def __init__(self, top_point, bottom_point, win):
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
        if self.has_left_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x1, self._y2)
            left_wall = Line(point_1, point_2)
            self._win.draw_line(left_wall, line_color)
        
        if self.has_right_wall:
            point_1 = Point(self._x2, self._y1)
            point_2 = Point(self._x2, self._y2)
            right_wall = Line(point_1, point_2)
            self._win.draw_line(right_wall, line_color)

        if self.has_top_wall:
            point_1 = Point(self._x1, self._y1)
            point_2 = Point(self._x2, self._y1)
            top_wall = Line(point_1, point_2)
            self._win.draw_line(top_wall, line_color)

        if self.has_bottom_wall:
            point_1 = Point(self._x1, self._y2)
            point_2 = Point(self._x2, self._y2)
            
            bottom_wall = Line(point_1, point_2)
            self._win.draw_line(bottom_wall, line_color)
