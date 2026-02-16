const { lengthOfLongestSubstring } = require('./solution')

describe('Longest Substring without repeating characters - Javascript', () => {
    test("Standard case: abcabcbb Expected output: 3", () => {
        const string = "abcabcbb"
        const result = lengthOfLongestSubstring(string)
        expect(result)
        self.assertEqual(result).toEqual(3)
    })
    test("All Same Characters case: bbbbb Expected output: 1", () => {
        const string = "bbbbb"
        const result = lengthOfLongestSubstring(string)
        expect(result)
        self.assertEqual(result).toEqual(1)
    })
    test("Another standard case: pwwkew Expected output: 3", () => {
        const string = "pwwkew"
        const result = lengthOfLongestSubstring(string)
        expect(result)
        self.assertEqual(result).toEqual(3)
    })
    test("Gold Standard case: abba Expected output: 2", () => {
        const string = "abba"
        const result = lengthOfLongestSubstring(string)
        expect(result)
        self.assertEqual(result).toEqual(2)
    })
    test("No repeating characters case: abcdefg Expected output: 7", () => {
        const string = "abcdefg"
        const result = lengthOfLongestSubstring(string)
        expect(result)
        self.assertEqual(result).toEqual(7)
    })
    test("Space and symbol diversity case: a b c a! Expected output: 4", () => {
        const string = "a b c a!"
        const result = lengthOfLongestSubstring(string)
        expect(result)
        self.assertEqual(result).toEqual(4)
    })
    test("Numerical mixed case: a b c a! Expected output: 6", () => {
        const string = "12312345!"
        const result = lengthOfLongestSubstring(string)
        expect(result)
        self.assertEqual(result).toEqual(6)
    })
    
})
