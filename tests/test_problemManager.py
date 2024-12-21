import unittest
from problem.problemManager import ProblemManager, ProblemType
from problem.problemDifficulty import ProblemDifficulty
from problem.addProblem import AddProblem

class TestProblemManager(unittest.TestCase):
    length, digits, choice_amount, choice_range = 1, 0, 1, 0

    def test_generate_numbers(self):
        problem_difficulty = ProblemDifficulty(self.length, self.digits, self.choice_amount, self.choice_range)
        problem_managera = ProblemManager(ProblemType.ADD, problem_difficulty, "hi")
        numbersa = problem_managera._generate_numbers()
        problem_managerb = ProblemManager(ProblemType.ADD, seed="hi")
        numbersb = problem_managerb._generate_numbers()
        self.assertEqual(numbersa, numbersb)
        problem_managera.difficulty.length = 5
        numbersa = problem_managera._generate_numbers()
        self.assertEqual(numbersa, [9, 7, 5, 7, 0])
        problem_managera.difficulty.digits = 0
        numbersa = problem_managera._generate_numbers()
        self.assertEqual(numbersa, [5, 8, 4, 3, 1])
        problem_managera.difficulty.digits = 1
        numbersa = problem_managera._generate_numbers()
        self.assertEqual(numbersa, [29, 17, 11, 21, 72])

    def test_generate_choices(self):
        problem_difficulty = ProblemDifficulty(self.length, self.digits, self.choice_amount, self.choice_range)
        problem_manager = ProblemManager(ProblemType.ADD, problem_difficulty, seed="bye")
        problem_manager.problem = AddProblem([10])
        problem_manager._generate_choices()
        self.assertEqual(problem_manager.choices, [10])
        problem_manager.difficulty.choice_amount = 5
        problem_manager._generate_choices()
        self.assertEqual(problem_manager.choices, [10, 10, 10, 10, 10])
        problem_manager.difficulty.choice_range = 1
        problem_manager._generate_choices()
        self.assertEqual(problem_manager.choices, [11, 10, 9, 9, 11])
        problem_manager.difficulty.choice_range = 8
        problem_manager._generate_choices()
        self.assertEqual(problem_manager.choices, [10, 18, 15, 4, 16])

    def test_check_choices(self):
        problem_manager = ProblemManager(ProblemType.ADD)
        problem_manager.problem = AddProblem([5, 6])
        self.assertTrue(problem_manager.check_choice(11))
        self.assertFalse(problem_manager.check_choice(5))

    def test_generate_problem(self):
        problem_difficulty = ProblemDifficulty(self.length, self.digits, self.choice_amount, self.choice_range)
        problem_manager = ProblemManager(ProblemType.ADD, problem_difficulty, "everything")
        problem_manager.generate_problem()
        expected_problem = AddProblem([8])
        self.assertEqual(problem_manager.problem, expected_problem)
        self.assertEqual(problem_manager.choices, [8])
        problem_manager.difficulty.length = 2
        problem_manager.difficulty.digits = 2
        problem_manager.difficulty.choice_amount = 2
        problem_manager.difficulty.choice_range = 2
        problem_manager.generate_problem()
        expected_problem.new_problem([168, 46])
        self.assertEqual(problem_manager.problem, expected_problem)
        self.assertEqual(problem_manager.choices, [214, 216])




if __name__ == "__main__":
    unittest.main()