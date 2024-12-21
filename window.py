import tkinter as tk


class Window():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.running = False
        self.root = tk.Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title("!!!Goblin Math!!!")
        self.root.config(bg = "green")
        self.canvas = tk.Canvas(self.root, width = width, height= height, bg = "green")
        tk.Canvas.pack(self.canvas, fill=tk.BOTH)
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False