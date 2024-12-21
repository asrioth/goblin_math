import tkinter as tk
from tkinter import ttk

class ProgressBar():
    def __init__(self, window, id, root, max = 100):
        self.progress = ttk.Progressbar(root, orient = tk.HORIZONTAL, 
              mode = 'determinate', maximum=max)
        self.value = 0
        self.max = max
        self.id = id
        self.window = window
        self.event = f"<<progress{self.id}>>"
    
    def pack(self, padx, pady, side):
        self.progress.pack(padx=padx, pady=pady, side=side, fill="x")

    def start(self):
        self.window.root.after(100, self.step)
    
    def reset(self):
        self.value = 0

    def step(self):
        self.value += 1
        self.progress.config(value=self.value)
        if (self.value < 100):
            self.window.root.after(100, self.step)
        else:
            self.window.root.event_generate(self.event)