"""
Finds two indices such that their values add up to the target.
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This dictionary stores: {value: index}
        seen_values = {}
        
        for index, num in enumerate(nums):
            # Calculate the "complement" needed to reach the target
            complement = target - num
            
            # Check if we have already encountered the complement
            if complement in seen_values:
                # If found, return the index of the complement and current index
                return [seen_values[complement], index]
            
            # Otherwise, store the current number and its index for future lookups
            seen_values[num] = index
            
        return [] # Return empty if no solution is found