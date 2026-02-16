/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    // Implement jump version using a set in js
    let charIndexSet = new Map()
    let left = 0
    let maxLen = 0

    for(var right = 0; right < s.length; right++) {
        const char = s[right];
        if(charIndexSet.has(char)) {
            // Jump 'left' to the right of the previous occurrence.
            // max() ensures we never jump BACKWARDS if the duplicate is outside the window.
            left = charIndexSet.get(char) + 1 > left ? charIndexSet.get(char) + 1 : left
            
        }
        // Update the map with the most recent position of this character
        charIndexSet.set(char, right)

        maxLen = maxLen > right - left + 1 ? maxLen : right - left + 1

    }
    return maxLen
};

module.exports = lengthOfLongestSubstring