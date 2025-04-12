from tkinter import Tk, BOTH, __canvas

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.__canvas = __canvas()
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_CLOSE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

def main():
    win = Window(800, 600)
    win.wait_for_close()

main()
