# 📔 Technical Notes: Two Sum

## 📊 Spreadsheet Data

- **Difficulty:** Easy
- **Pattern:** Hash Map (Complements)
- **Time Complexity:** O(n)
- **Space Complexity:** O(n)
- **Verdict:** One-pass Hash Map is optimal.

## 🧠 The Logic "Aha!" Moment

Initially, I thought about using a nested loop. However, the bottleneck there is searching for the second number.

**The Insight:** Instead of asking "Where is the other number?", we store what we've already seen in a Hash Map so we can find it in O(1) time later.

## 🚧 Trial & Error (My Process)

1. **Attempt 1** (Brute Force): Used two for loops. It worked but was too slow (O(n^2)).
2. **Attempt 2** (Two-Pass Hash Map): First, I added all numbers to the map, then I looked for complements. This worked but had a bug: I accidentally used the same element twice (e.g., target 6, found 3 at index 0 and used it again).
3. **Final Attempt (One-Pass):** Add to the map as I go. This naturally prevents using the same index twice.

---

## ⚠️ Edge Cases to Mention in Blog

- **Negative Numbers:** Does it work for target = -5? Yes, the math remains the same.

- **Duplicates:** If the array is [3, 3] and the target is 6, the map needs to handle the indices correctly.

- **No Solution:** Though the problem says one exists, in real code, I should return an empty list or null.

## 💡 Real-World Analogy for Blog

Think of a **"Missing Person" list.**
As you walk through a crowd (the array), you look at each person's face. You check your list to see if anyone is looking for the person currently standing in front of you. If not, you write down that person's name and where you saw them (index) so the next person in the crowd can check against it.

## 🔗 Portfolio Connections

- **Related Patterns:** Two Pointers (if sorted), 3Sum

- **Skills Demonstrated:** Data Structure selection, Time-Space trade-off analysis.