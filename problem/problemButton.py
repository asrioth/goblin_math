import tkinter as tk
from button import Button
from problem.problemManager import ProblemManager

class ProblemButton(Button):
    def __init__(self, window, name, problem_manager):
        super().__init__(window, name)
        self.problem_manager = problem_manager
    
    def clicked(self):
        if self.problem_manager.check_choice(self.name):
            self.button.config(text="***Monch***")
        else:
            self.button.config(text="***blegh***", disabledforeground="purple")
        self.button.config(bg="green", relief=tk.FLAT, highlightthickness=0, state="disabled")