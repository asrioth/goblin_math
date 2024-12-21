import tkinter as tk

class Label():
    def __init__(self, win, string_var):
        self.label = tk.Label(win.canvas,
                 textvariable=string_var.text_var,
                 anchor=tk.CENTER,
                 bg="green",
                 height=2,
                 #width=15,
                 bd=3,
                 font=("Arial", 12),
                 cursor="arrow",
                 fg="black",
                 padx=15,
                 pady=15,
                 justify=tk.CENTER,
                 relief=tk.FLAT,
                 underline=-1,
                 wraplength=250
                )
        
    def pack(self, padx, pady, side):
        self.label.pack(padx=padx, pady=pady, side=side)