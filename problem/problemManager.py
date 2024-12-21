from enum import Enum
from problem.addProblem import AddProblem
from problem.problemDifficulty import ProblemDifficulty
import random

class ProblemType(Enum):
    ADD = "Add"

class ProblemManager():
    def __init__(self, problem_type, problem_difficulty = None, seed = None):
        self.problem_type = problem_type
        self.difficulty = problem_difficulty
        if problem_difficulty == None:
            self.difficulty = ProblemDifficulty()
        self.problem = None
        self.choices = None
        if seed != None:
            random.seed(seed)

    def generate_problem(self):
        match self.problem_type:
            case ProblemType.ADD:
                numbers = self._generate_numbers()
                self.problem = AddProblem(numbers)
                self._generate_choices()
            case _:
                raise Exception("Unrecognized problem")
        
    def _generate_numbers(self):
        numbers = []
        for _ in range(self.difficulty.length):
            numbers.append(random.randint(0, (9 * (10 * self.difficulty.digits) + 9)))
        return numbers
    
    def _generate_choices(self):
        choices = [self.problem.answer]
        for _ in range(self.difficulty.choice_amount-1):
            choices.append(random.randint(self.problem.answer - self.difficulty.choice_range, self.problem.answer + self.difficulty.choice_range))
        random.shuffle(choices)
        self.choices = choices

    def check_choice(self, choice):
        return choice == self.problem.answer