import tkinter as tk
from problem.problemDifficulty import ProblemDifficulty
from problem.problemManager import ProblemManager, ProblemType
from stringVar import StringVar
from label import Label
from problem.problemButton import ProblemButton
from progressBar import ProgressBar
from problem.problemFrame import ProblemFrame
import random

class GuiManager():
    def __init__(self, window):
        self.window = window
        self.resource_label = None
        self.frames = {}
        

    def create_problem(self, goblin, event = None):
        goblin.problem_manager.generate_problem()
        if goblin.id not in self.frames:
            self._create_new_problem(goblin)
        else:
            self.frames[goblin.id].labels[0].update_text(goblin.problem_manager.problem.display)
            for button in self.frames[goblin.id].buttons:
                button.destroy()
            self.frames[goblin.id].buttons = []
            self.frames[goblin.id].progress_bar.reset()
            #self.frames[goblin.id].progress_bar.update_progress_step(goblin.shop.progress_bar_time_step)
        self._create_problem_buttons(goblin)
        if not goblin.is_user:
            goblin.solve_problem()
            self.window.root.after(random.randint(1000, 9000), lambda : self.hit_button(goblin))
        self.frames[goblin.id].progress_bar.start()
    
    def _pick_goblin_frame_side(self, goblin):
        if goblin.is_user:
            side = tk.BOTTOM
        else:
            side = tk.TOP
        return side

    def _create_new_problem(self, goblin):
        problem_frame = ProblemFrame(goblin.id)
        frame = tk.Frame(self.window.canvas, bg="green")
        side = self._pick_goblin_frame_side(goblin)
        frame.pack(fill=tk.BOTH, expand=True, side=side)
        problem_frame.frame = frame
        problem_var = StringVar(goblin.problem_manager.problem.display)
        problem_label = Label(frame, problem_var)
        problem_label.pack(20, 20, tk.LEFT)
        problem_frame.labels.append(problem_label)
        progres_bar = ProgressBar(self.window, goblin.id, frame, goblin.shop.progress_bar_time_step)
        progres_bar.pack(20, 20, tk.TOP)
        event = "<<update_time_step>>"
        self.window.root.bind(event, lambda event: progres_bar.update_progress_step(goblin.shop.progress_bar_time_step))
        self.window.root.bind(progres_bar.event, lambda event: self.create_problem(goblin))
        problem_frame.progress_bar = progres_bar
        self.frames[problem_frame.id] = problem_frame


    def _create_problem_buttons(self, goblin):
        for choice in goblin.problem_manager.choices:
            problem_button = ProblemButton(self.frames[goblin.id].frame, choice, goblin)
            problem_button.pack(20, 20, tk.LEFT)
            self.frames[goblin.id].buttons.append(problem_button)

    def hit_button(self, goblin):
        self.frames[goblin.id].buttons[goblin.answer_index].clicked()