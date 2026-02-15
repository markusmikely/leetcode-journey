import unittest
from solution import Solution  # Assumes your code is in solution.py

class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_standard(self):
        """Standard case: abcabcbb Expected output: 3"""
        string = "abcabcbb"
        result = self.sol.lengthOfLongestSubstring(string)
        self.assertEqual(result, 3)

    def test_all_same_characters(self):
        """All Same Characters case: bbbbb Expected output: 1"""
        string = "bbbbb"
        result = self.sol.lengthOfLongestSubstring(string)
        self.assertEqual(result, 1)

    def test_another_standard(self):
        """Another standard case: pwwkew Expected output: 3"""
        string = "pwwkew"
        result = self.sol.lengthOfLongestSubstring(string)
        self.assertEqual(result, 3)

    def test_gold_standard(self):
        """Gold Standard case: abba Expected output: 2"""
        string = "abba"
        result = self.sol.lengthOfLongestSubstring(string)
        self.assertEqual(result, 2)
    
    def test_no_repeating_chars(self):
        """No repeating characters case: abcdefg Expected output: 7"""
        string = "abcdefg"
        result = self.sol.lengthOfLongestSubstring(string)
        self.assertEqual(result, 7)

    def test_space_and_symbol_diversity(self):
        """Space and symbol diversity case: a b c a! Expected output: 5"""
        string = "a b c a!"
        result = self.sol.lengthOfLongestSubstring(string)
        self.assertEqual(result, 4)

    def test_numerical_mixed_case(self):
        """Numerical mixed case: a b c a! Expected output: 6"""
        string = "12312345!"
        result = self.sol.lengthOfLongestSubstring(string)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()