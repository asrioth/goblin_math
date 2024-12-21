import unittest
from resourceManager import ResourceManager
import math
from problem.problemDifficulty import ProblemDifficulty

class testResourceManager(unittest.TestCase):

    def test_calculate_length_crunches(self):
        resource_manager = ResourceManager()
        length_crunches = math.floor(resource_manager._calculate_length_crunches(1, 1))
        expected_crunches = 1
        self.assertEqual(length_crunches, expected_crunches)
        length_crunches = math.floor(resource_manager._calculate_length_crunches(4, 1))
        expected_crunches = 2
        self.assertEqual(length_crunches, expected_crunches)
        resource_manager = ResourceManager()
        length_crunches = math.ceil(resource_manager._calculate_length_crunches(1, -1))
        expected_crunches = -1
        self.assertEqual(length_crunches, expected_crunches)
        resource_manager = ResourceManager()
        length_crunches = math.ceil(resource_manager._calculate_length_crunches(4, -1))
        expected_crunches = -2
        self.assertEqual(length_crunches, expected_crunches)
    
    def test_calculate_digits_crunches(self):
        resource_manager = ResourceManager()
        digits_crunches = math.floor(resource_manager._calculate_digits_crunches(0, 1))
        expected_crunches = 1
        self.assertEqual(digits_crunches, expected_crunches)
        resource_manager = ResourceManager()
        digits_crunches = math.floor(resource_manager._calculate_digits_crunches(1, 1))
        expected_crunches = 2
        self.assertEqual(digits_crunches, expected_crunches)
        digits_crunches = math.floor(resource_manager._calculate_digits_crunches(3, 1))
        expected_crunches = 7
        self.assertEqual(digits_crunches, expected_crunches)
        digits_crunches = math.ceil(resource_manager._calculate_digits_crunches(0, -1))
        expected_crunches = -1
        self.assertEqual(digits_crunches, expected_crunches)
        resource_manager = ResourceManager()
        digits_crunches = math.ceil(resource_manager._calculate_digits_crunches(1, -1))
        expected_crunches = -2
        self.assertEqual(digits_crunches, expected_crunches)
        digits_crunches = math.ceil(resource_manager._calculate_digits_crunches(3, -1))
        expected_crunches = -7
        self.assertEqual(digits_crunches, expected_crunches)

    def test_calculate_choices_crunches(self):
        resource_manager = ResourceManager()
        choice_crunches =  resource_manager._calculate_choice_crunches(1, 0, 1)
        expected_crunches = 1
        self.assertEqual(choice_crunches, expected_crunches)
        choice_crunches =  resource_manager._calculate_choice_crunches(5, 0, 1)
        expected_crunches = 1
        self.assertEqual(choice_crunches, expected_crunches)
        choice_crunches =  resource_manager._calculate_choice_crunches(1, 5, 1)
        expected_crunches = 1
        self.assertEqual(choice_crunches, expected_crunches)
        choice_crunches =  resource_manager._calculate_choice_crunches(2, 1, 1)
        expected_crunches = 1.5
        self.assertEqual(choice_crunches, expected_crunches)
        choice_crunches =  resource_manager._calculate_choice_crunches(5, 1, 1)
        expected_crunches = 2.4
        self.assertEqual(choice_crunches, expected_crunches)
        choice_crunches =  resource_manager._calculate_choice_crunches(2, 2, 1)
        expected_crunches = 2.5
        self.assertEqual(choice_crunches, expected_crunches)
        choice_crunches =  resource_manager._calculate_choice_crunches(2, 5, 1)
        expected_crunches = 5.5
        self.assertEqual(choice_crunches, expected_crunches)
        choice_crunches =  resource_manager._calculate_choice_crunches(5, 0, -1)
        expected_crunches = -1
        self.assertEqual(choice_crunches, expected_crunches)
        choice_crunches =  resource_manager._calculate_choice_crunches(1, 5, -1)
        expected_crunches = -1
        self.assertEqual(choice_crunches, expected_crunches)
        choice_crunches =  resource_manager._calculate_choice_crunches(2, 5, -1)
        expected_crunches = -5.5
        self.assertEqual(choice_crunches, expected_crunches)

    def test_update_crunches(self):
        resource_manager = ResourceManager()
        problem_difficulty = ProblemDifficulty(length = 1,digits = 0,choice_amount = 1,choice_range = 0)
        resource_manager.update_crunches(problem_difficulty, True)
        expected_crunches = 1
        self.assertAlmostEqual(resource_manager.crunches, expected_crunches, delta=0.1)
        resource_manager.crunches = 0
        problem_difficulty = ProblemDifficulty(length = 31,digits = 0,choice_amount = 1,choice_range = 0)
        resource_manager.update_crunches(problem_difficulty, True)
        expected_crunches = 2
        self.assertAlmostEqual(resource_manager.crunches, expected_crunches, delta=0.1)
        resource_manager.crunches = 0
        problem_difficulty = ProblemDifficulty(length = 1,digits = 2,choice_amount = 1,choice_range = 0)
        resource_manager.update_crunches(problem_difficulty, True)
        expected_crunches = 2
        self.assertAlmostEqual(resource_manager.crunches, expected_crunches, delta=0.5)
        resource_manager.crunches = 0
        problem_difficulty = ProblemDifficulty(length = 1,digits = 0,choice_amount = 2,choice_range = 4)
        resource_manager.update_crunches(problem_difficulty, True)
        expected_crunches = 2
        self.assertAlmostEqual(resource_manager.crunches, expected_crunches, delta=0.3)
        resource_manager.crunches = 0
        problem_difficulty = ProblemDifficulty(length = 1,digits = 0,choice_amount = 1,choice_range = 0)
        resource_manager.update_crunches(problem_difficulty, False)
        expected_crunches = -1
        self.assertAlmostEqual(resource_manager.crunches, expected_crunches, delta=0.1)
        resource_manager.crunches = 0
        problem_difficulty = ProblemDifficulty(length = 31,digits = 0,choice_amount = 1,choice_range = 0)
        resource_manager.update_crunches(problem_difficulty, False)
        expected_crunches = -2
        self.assertAlmostEqual(resource_manager.crunches, expected_crunches, delta=0.1)
        resource_manager.crunches = 0
        problem_difficulty = ProblemDifficulty(length = 1,digits = 2,choice_amount = 1,choice_range = 0)
        resource_manager.update_crunches(problem_difficulty, False)
        expected_crunches = -2
        self.assertAlmostEqual(resource_manager.crunches, expected_crunches, delta=0.5)
        resource_manager.crunches = 0
        problem_difficulty = ProblemDifficulty(length = 1,digits = 0,choice_amount = 2,choice_range = 4)
        resource_manager.update_crunches(problem_difficulty, False)
        expected_crunches = -2
        self.assertAlmostEqual(resource_manager.crunches, expected_crunches, delta=0.3)
        problem_difficulty = ProblemDifficulty(length = 1,digits = 0,choice_amount = 2,choice_range = 4)
        resource_manager.update_crunches(problem_difficulty, False)
        expected_crunches = -4
        self.assertAlmostEqual(resource_manager.crunches, expected_crunches, delta=0.5)