from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)

    line1 = Line(Point(100, 100), Point(300, 300))
    win.draw_line(line1, "black")
    
    line2 = Line(Point(200, 100), Point(200, 400))
    win.draw_line(line2, "red")
    
    line3 = Line(Point(300, 200), Point(500, 200))
    win.draw_line(line3, "blue")

    win.wait_for_close()

if __name__ == "__main__":
    main()