import tkinter as tk

class StringVar():
    def __init__(self, text):
        self.text = text
        self.text_var = tk.StringVar()
        self.text_var.set(text)