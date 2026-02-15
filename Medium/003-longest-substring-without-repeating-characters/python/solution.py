class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Implement jump version
        char_index_map = {} # stores { character: index }
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in char_index_map:
                # Jump 'left' to the right of the previous occurrence.
                # max() ensures we never jump BACKWARDS if the duplicate is outside the window.
                left = max(char_index_map[char] + 1, left)
            
            # Update the map with the most recent position of this character
            char_index_map[char] = right

            max_len = max(max_len, right - left + 1)

        return max_len
            