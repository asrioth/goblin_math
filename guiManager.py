import tkinter as tk
from problem.problemDifficulty import ProblemDifficulty
from problem.problemManager import ProblemManager, ProblemType
from stringVar import StringVar
from label import Label
from problem.problemButton import ProblemButton
from progressBar import ProgressBar

class GuiManager():
    def __init__(self, window, problem_manager):
        self.window = window
        self.problem_manager = problem_manager
        self.progres_bar = ProgressBar(window, 0)
        self.progres_bar.pack(20, 20, tk.TOP)
        self.labels = []
        self.buttons = []

    def create_problem(self, what = None):
        self.problem_manager.generate_problem()
        if self.labels == [] or self.buttons == []:
            self._create_new_problem()
        else:
            self.labels[0].update_text(self.problem_manager.problem.display)
            for button in self.buttons:
                button.destroy()
            self.progres_bar.reset()
        self._create_problem_buttons()
        self.progres_bar.start()
    
    def _create_new_problem(self):
        problem_var = StringVar(self.problem_manager.problem.display)
        problem_label = Label(self.window, problem_var)
        self.labels.append(problem_label)
        problem_label.pack(20, 20, tk.LEFT)

    def _create_problem_buttons(self):
        for choice in self.problem_manager.choices:
            problem_button = ProblemButton(self.window, choice, self.problem_manager)
            self.buttons.append(problem_button)
            problem_button.pack(20, 20, tk.LEFT)