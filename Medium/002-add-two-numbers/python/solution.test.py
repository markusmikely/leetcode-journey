import unittest
from solution import Solution  # Assumes your code is in solution.py

# Helper to convert list to Linked List
def to_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper to convert Linked List back to Python list for easy comparison
def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_standard(self):
        """Standard case: 342 + 465 = 807"""
        l1 = to_linked_list([2, 4, 3])
        l2 = to_linked_list([5, 6, 4])
        result = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(to_list(result), [7, 0, 8])

    def test_different_lengths(self):
        """One number is longer than the other"""
        l1 = to_linked_list([9, 9])
        l2 = to_linked_list([1])
        result = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(to_list(result), [0, 0, 1])

    def test_final_carry(self):
        """Carry results in an extra digit at the end"""
        l1 = to_linked_list([5])
        l2 = to_linked_list([5])
        result = self.sol.addTwoNumbers(l1, l2)
        self.assertEqual(to_list(result), [0, 1])

if __name__ == "__main__":
    unittest.main()