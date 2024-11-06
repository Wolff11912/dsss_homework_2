import unittest
from math_quiz import randomInteger, randomOperator, calculator


class TestMathGame(unittest.TestCase):

    def test_randomInteger(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomInteger(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_randomOperator(self):
        # Test if one of the listed operators is picked
        for _ in range(1000):
             picked_operator = randomOperator()
             self.assertTrue(picked_operator in ['+', '-', '*'])

    def test_calculator(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (9, 4, '-', '9 - 4', 5),
                (8, 3, '*', '8 * 3', 24),
                (4, -6, '+', '4 + -6', -2),
                (-3, -7, '-', '-3 - -7', 4),
                (-2, 10, '*', '-2 * 10', -20)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calculator(num1, num2, operator)
                self.assertTrue((expected_problem == problem) and (answer == expected_answer))

if __name__ == "__main__":
    unittest.main()
