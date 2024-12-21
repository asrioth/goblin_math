import tkinter as tk
from button import Button
from problem.problemManager import ProblemManager

class ProblemButton(Button):
    def __init__(self, root, name, goblin):
        super().__init__(root, name)
        self.goblin = goblin
    
    def clicked(self):
        self.goblin.resource_manager.click_detected()
        if self.goblin.problem_manager.check_choice(self.name):
            self.button.config(text="***Monch***")
            self.goblin.monch()
        else:
            self.button.config(text="***blegh***", disabledforeground="purple")
            self.goblin.blegh()
        self.button.config(bg="green", relief=tk.FLAT, highlightthickness=0, state="disabled")

    def destroy(self):
        super().destroy()
    
    def __repr__(self):
        return super().__repr__()