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
        self.user_frame = tk.Frame(self.root)
        self.user_frame.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)
        self.canvas = tk.Canvas(self.user_frame, width = width, height= height, bg = "green")
        tk.Canvas.pack(self.canvas, fill=tk.BOTH, expand=True)
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