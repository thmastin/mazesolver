from window import Window
from line import Line
from point import Point
from cell import Cell

def main():
    win = Window(800, 600)
    
    cell_1 = Cell(Point(50, 50), Point(100, 100), win)
    cell_1.draw()

    cell_2 = Cell(Point(100, 100), Point(200, 200), win)
    cell_2.draw()

    cell_3 = Cell(Point(50,100), Point(100,150), win)
    cell_3.has_right_wall = False
    cell_3.draw()

    cell_1.draw_move(cell_2)
    cell_2.draw_move(cell_3, True)
    

    win.wait_for_close()

if __name__ == "__main__":
    main()