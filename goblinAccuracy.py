import math
import random
from problem.problemDifficulty import ProblemDifficulty
from problem.problemManager import ProblemType

class GoblinAccuracy():
    def __init__(self, max_accuracy, problem_comprehension, problem_difficulty):
        self.max = max_accuracy
        self.current = 0
        self.problem_difficulty = problem_difficulty
        self.problem_comprehension = problem_comprehension
        self.id = 0
        self._set_id()
        self.set_current_accuracy()

    def _set_id(self):
        l, d, ca, cr = self.problem_difficulty.length, self.problem_difficulty.digits, self.problem_difficulty.choice_amount, self.problem_difficulty.choice_range
        id_string = f"{l}{d}{ca}{cr}"
        self.id = int(id_string)

    def does_hit(self):
        spot = random.randint(0, 100) / 100
        return spot <= self.current

    def set_current_accuracy(self):
        base_comprehension = self.base_comprehension()
        if base_comprehension == 1:
            self.current = self.max
            return
        base_hit_accuracy = self.base_hit_accuracy()
        comprehension_accuracy = base_comprehension * self.max
        hit_accuracy = (self.max - comprehension_accuracy) * base_hit_accuracy
        self.current = comprehension_accuracy + hit_accuracy
        
    def base_comprehension(self):
        length_mod = max(0.5 / self.problem_difficulty.length, self.problem_comprehension/2)
        digit_mod = max(0.5 / ((self.problem_difficulty.digits * 10) + 1), self.problem_comprehension/2)
        base_chomprehension = length_mod + digit_mod
        return base_chomprehension

    def base_hit_accuracy(self):
        if self.problem_difficulty.choice_amount == 0 or self.problem_difficulty.choice_range == 0:
            return 1 * self.current
        dynamic_choices = self.problem_difficulty.choice_amount - 1
        incorrect_possibilities = 2 * self.problem_difficulty.choice_range
        denominator = pow(incorrect_possibilities + 1, dynamic_choices)
        total_accuracy = ((math.pow(incorrect_possibilities, dynamic_choices)) / denominator) * (1/self.problem_difficulty.choice_amount)
        for num_correct in range(2, self.problem_difficulty.choice_amount-1):
            num_correct_probability = (pow(incorrect_possibilities, self.problem_difficulty.choice_amount - num_correct) * dynamic_choices) / denominator
            total_accuracy += num_correct_probability * (num_correct / self.problem_difficulty.choice_amount)
        total_accuracy += 1/denominator
        return total_accuracy