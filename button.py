import tkinter as tk
from window import Window

class Button():
    def __init__(self, root, name):
        self.button = tk.Button(root, 
                   text=name,
                   command=self.clicked,
                   activebackground="red",
                   activeforeground="white",
                   anchor="center",
                   bd=3,
                   bg="lightgray",
                   cursor="hand2",
                   disabledforeground="black",
                   fg="black",
                   font=("Arial", 12),
                   height=2,
                   highlightbackground="black",
                   highlightcolor="green",
                   highlightthickness=2,
                   justify="center",
                   overrelief="raised",
                   padx=20,
                   pady=5,
                   #width=15,
                   wraplength=150)
        self.name = name
        self.root = root
    
    def clicked(self):
        print(f"{self.name} clicked!")

    def pack(self, padx, pady, side):
        self.button.pack(padx=padx, pady=pady, side=side)

    def destroy(self):
        self.button.destroy()

    def __repr__(self):
        return f"button({self.name})"