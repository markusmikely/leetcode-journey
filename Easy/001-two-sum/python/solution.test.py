import unittest
from solution import Solution  # Assumes your code is in solution.py

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_standard_case(self):
        """Standard positive integers"""
        self.assertEqual(self.sol.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_negative_numbers(self):
        """Ensure it handles negative values correctly"""
        self.assertEqual(self.sol.twoSum([-3, 4, 3, 90], 0), [0, 2])

    def test_duplicates(self):
        """Case where the two numbers are the same value"""
        self.assertEqual(self.sol.twoSum([3, 3], 6), [0, 1])

    def test_large_target(self):
        """Testing larger numbers"""
        self.assertEqual(self.sol.twoSum([10, 20, 30, 40, 50], 90), [3, 4])

    def test_no_solution(self):
        """Handle cases where no pair exists (if your code returns [])"""
        self.assertEqual(self.sol.twoSum([1, 2, 3], 7), [])

if __name__ == "__main__":
    unittest.main()