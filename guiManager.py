import tkinter as tk
from problem.problemDifficulty import ProblemDifficulty
from problem.problemManager import ProblemManager, ProblemType
from stringVar import StringVar
from label import Label
from problem.problemButton import ProblemButton
from progressBar import ProgressBar
from problem.problemFrame import ProblemFrame

class GuiManager():
    def __init__(self, window):
        self.window = window
        self.frames = {}

    def create_problem(self, goblin, what = None):
        goblin.problem_manager.generate_problem()
        if goblin.id not in self.frames:
            self._create_new_problem(goblin)
        else:
            self.frames[goblin.id].labels[goblin.id].update_text(goblin.problem_manager.problem.display)
            for button in self.frames[goblin.id].buttons:
                button.destroy()
            self.frames[goblin.id].buttons = []
            self.frames[goblin.id].progress_bar.reset()
        self._create_problem_buttons(goblin)
        self.frames[goblin.id].progress_bar.start()
    
    def _create_new_problem(self, goblin):
        problem_frame = ProblemFrame(goblin.id)
        frame = tk.Frame(self.window.canvas, bg="green")
        frame.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)
        problem_frame.frame = frame
        problem_var = StringVar(goblin.problem_manager.problem.display)
        problem_label = Label(frame, problem_var)
        problem_label.pack(20, 20, tk.LEFT)
        problem_frame.labels.append(problem_label)
        progres_bar = ProgressBar(self.window, goblin.id, frame)
        progres_bar.pack(20, 20, tk.TOP)
        self.window.root.bind(progres_bar.event, lambda event: self.create_problem(goblin))
        problem_frame.progress_bar = progres_bar
        self.frames[problem_frame.id] = problem_frame


    def _create_problem_buttons(self, goblin):
        for choice in goblin.problem_manager.choices:
            problem_button = ProblemButton(self.frames[goblin.id].frame, choice, goblin.problem_manager)
            problem_button.pack(20, 20, tk.LEFT)
            self.frames[goblin.id].buttons.append(problem_button)