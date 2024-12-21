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
from goblin import Goblin
from resourceManager import ResourceManager
import math

def main():
    win = Window(800, 600)
    problem_difficulty = ProblemDifficulty(length=2, choice_range=1, choice_amount=5, digits=1)
    problem_manager = ProblemManager(ProblemType.ADD, problem_difficulty)
    problem_manager2 = ProblemManager(ProblemType.ADD)
    resource_manager = ResourceManager()
    goblin = Goblin(problem_manager, resource_manager, 0, True)
    goblin2 = Goblin(problem_manager2, resource_manager, 1, False)
    gui_manager = GuiManager(win, resource_manager)
    gui_manager.create_problem(goblin)
    gui_manager.create_problem(goblin2)
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