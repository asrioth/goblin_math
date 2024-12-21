import unittest
import tests.test_problemManager
import tkinter as tk
from window import Window
from button import Button
from label import Label
from stringVar import StringVar
from problem.addProblem import AddProblem
from problem.problemManager import ProblemManager, ProblemType
from problem.problemButton import ProblemButton
from problem.problemDifficulty import ProblemDifficulty
from progressBar import ProgressBar
from guiManager import GuiManager

def main():
    win = Window(800, 600)
    problem_difficulty = ProblemDifficulty(length=2, choice_range=1, choice_amount=5, digits=1)
    problem_manager = ProblemManager(ProblemType.ADD, problem_difficulty)
    gui_manager = GuiManager(win, problem_manager)
    gui_manager.create_problem()
    win.root.bind("<<progress0>>", gui_manager.create_problem)
    win.root.bind()
    """problem_manager.generate_problem()
    problem_var = StringVar(problem_manager.problem.display)
    problem_label = Label(win, problem_var)
    problem_label.pack(20, 20, tk.LEFT)
    for choice in problem_manager.choices:
        problem_button = ProblemButton(win, choice, problem_manager)
        problem_button.pack(20, 20, tk.LEFT)"""
    win.wait_for_close()

if __name__ == "__main__":
    main()