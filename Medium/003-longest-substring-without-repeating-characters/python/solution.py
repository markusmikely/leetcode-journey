class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window technique - O(n)
        # init left and right pointers
        # O(n) - Very Fast
        # char_set = set()
        # left = 0
        # max_len = 0
        # for right in range(len(s)):
        #     # If the current character is already in the window, 
        #     # shrink from the left until it's gone.
        #     while s[right] in char_set:
        #         char_set.remove(s[left])
        #         left += 1

        #     # Now that it's unique, add it and update the length
        #     char_set.add(s[right])

        #     # Length of window is always: (right - left + 1)
        #     max_len = max(max_len, right - left + 1)

        # return max_len


        # Implment jump version
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
            