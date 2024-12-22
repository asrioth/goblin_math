import tkinter as tk
from button import Button
from problem.problemManager import ProblemManager
from resourceManager import Resource

class ProblemButton(Button):
    def __init__(self, root, answer, goblin):
        super().__init__(root, answer)
        self.goblin = goblin
        if not goblin.is_user:
            self.button.config(state="disabled", bg="green")
        self.event = "<<update_resouce_display>>"
    
    def clicked(self):
        match self.goblin.eat_answer(self.name):
            case Resource.MONCH:
                self.button.config(text=self.goblin.monch_display, disabledforeground="red")
            case Resource.BLEGH:
                self.button.config(text=self.goblin.blegh_display, disabledforeground="purple")
        self.button.config(bg="green", relief=tk.FLAT, highlightthickness=0, state="disabled", cursor="X_cursor")
        self.root.event_generate(self.event)

    def destroy(self):
        super().destroy()
    
    def __repr__(self):
        return super().__repr__()