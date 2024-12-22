import tkinter as tk
from tkinter import ttk
import math

class ProgressBar():
    def __init__(self, window, id, root, progress_step = 1):
        self._set_styles()
        self.max = 100
        self.time_progress = ttk.Progressbar(root, orient = tk.HORIZONTAL, 
              mode = "determinate", maximum=self.max, style="time.bar.Horizontal.TProgressbar")
        self.step_progress = ttk.Progressbar(root, orient = tk.HORIZONTAL, 
              mode = "indeterminate", maximum=1, style="step.bar.Horizontal.TProgressbar")
        self.step_progress.config(value=0)
        self.step_progress.bind("<Button-1>", self.move_step_progress)
        self.event = "<<update_resouce_display>>"
        self.value = 0
        self.current_progress_step = progress_step
        self.progress_steps = [progress_step]
        self.id = id
        self.window = window
        self.root = root
        self.event = f"<<progress{self.id}>>"
    
    def move_step_progress(self, event):
        length = int(self.step_progress.winfo_geometry().split("+")[0].split("x")[0])
        bar_percent = round((event.x / length) * len(self.progress_steps))
        index = round((event.x / length) * (len(self.progress_steps)-1))
        self.current_progress_step = self.progress_steps[index]
        self.step_progress.config(value=bar_percent)


    def _set_styles(self):
        style = ttk.Style()
        troughcolor = "green"
        bordercolor = "dark green"
        background = "royal blue"
        lightcolor = "cornflower blue"
        darkcolor = "blue"
        style.configure("time.bar.Horizontal.TProgressbar", troughcolor=troughcolor, 
                bordercolor=bordercolor, background=background, lightcolor=lightcolor, 
                darkcolor=darkcolor)
        step_background = "purple"
        step_lightcolor = "dark orchid"
        step_darkcolor = "purple4"
        style.configure("step.bar.Horizontal.TProgressbar", troughcolor=troughcolor, 
                bordercolor=bordercolor, background=step_background, lightcolor=step_lightcolor, 
                darkcolor=step_darkcolor)

    def update_progress_step(self, new_step):
        if self.current_progress_step != new_step:
            self.current_progress_step = new_step
            self.progress_steps.append(new_step)
            self.step_progress.config(maximum=len(self.progress_steps), value=len(self.progress_steps))

    def pack(self, padx, pady, side):
        self.step_progress.pack(padx=padx, pady=pady, side=side, fill="x")
        self.time_progress.pack(padx=padx, pady=pady, side=side, fill="x")

    def start(self):
        self.window.root.after(100, self.step)
    
    def reset(self):
        self.value = 0

    def step(self):
        self.value += self.current_progress_step
        self.time_progress.config(value=self.value)
        if (self.value < self.max):
            self.window.root.after(100, self.step)
        else:
            self.window.root.event_generate(self.event)