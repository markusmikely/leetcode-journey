# 📔 Technical Notes: Two Sum

## 📊 Spreadsheet Data

- **Difficulty:** Medium
- **Pattern:** Optimized Sliding Window (Two-Pointer Jump)
- **Time Complexity:** $O(n)$ — Each character is visited once by the "right" pointer.
- **Space Complexity:** $O(min(m, n))$ — $m$ is the character set (ASCII 128/256) and $n$ is the string length.
- **Verdict:** The Hash Map "Jump" variation is optimal. It prevents redundant re-scanning of the string that occurs in a basic sliding window.

## 🧠 The Logic "Aha!" Moment

Initially, I considered a brute-force approach: checking every possible substring for duplicates. However, the bottleneck is $O(n^3)$ or $O(n^2)$ complexity, which fails on large inputs.

**The Insight:** Instead of sliding the left pointer one-by-one, we can store the last seen index of every character in a Hash Map. When a duplicate is found, we "jump" the left pointer directly to $last\_seen + 1$. This turns the process into a single, efficient pass.

## 🚧 Trial & Error (My Process)

1. **Attempt 1 (Brute Force):** Nested loops to check all substrings. (Inefficient: $O(n^2)$).
2. **Attempt 2 (Standard Sliding Window):** Used a set() and a while loop to shrink the window from the left. Worked well, but still required multiple increments of the left pointer ($O(2n)$).
3. **Final Attempt (Jump):** Used a dict to store indices, allowing the left pointer to teleport to the correct position in $O(1)$.

---

## ⚠️ Edge Cases to Mention in Blog

- **The "abba" Trap:** If you find a duplicate that occurred before your current window started, you must not jump the left pointer backward. Using `max(left, last_seen + 1)` is the critical guard here.

- **Symbol & Digit Diversity:** Since the input includes spaces and symbols, a Hash Map is safer than a fixed-size array unless the character set is strictly defined (e.g., ASCII 128).

- **Empty Strings:** The algorithm must return `0` for an empty input string without crashing.

## 💡 Real-World Analogy for Blog

Think of a **"Unique Guest List"** at a party entrance.
Think of a "Unique Guest List" at a party entrance.
As people walk in, you keep a log of their names and their position in line. If someone tries to enter who is **already inside**, you don't just ask them to leave; you instantly know exactly where the first instance of that person is in the room and you can "reset" your count from the person immediately following them.

## 🔗 Portfolio Connections

- **Related Patterns:** Two Pointers, Fixed-size Array Optimization.

- **Skills Demonstrated:** Efficient window management, Hash Table lookups, and Pythonic iteration (enumerate).