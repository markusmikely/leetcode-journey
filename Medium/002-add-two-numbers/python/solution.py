"""
Adds two numbers stored in a linked list and return the list as a new linked list
Time Complexity: O(max(m, n))
Space Complexity: O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Anchor (Dummy) node acts as a starting point to build our result list
        anchor = ListNode(0)
        curr = anchor
        carry = 0
        
        # We continue as long as there are digits to add or a carry remaining
        while l1 or l2 or carry:
            # Extract values, defaulting to 0 if a list is shorter than the other
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # divmod handles the math in one step:
            # quotient (carry) for the next iteration, remainder (out) for the current node
            carry, out = divmod(val1 + val2 + carry, 10)
            
            # Create the next node and move the 'curr' pointer forward
            curr.next = ListNode(out)
            curr = curr.next
            
            # Advance the input pointers if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
    
        # Return the 'next' of anchor because anchor itself was just a placeholder
        return anchor.next