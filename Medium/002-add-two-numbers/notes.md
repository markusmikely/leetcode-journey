# 📔 Technical Notes: Add Two Numbers

## 📊 Spreadsheet Data

- **Difficulty:** Medium
- **Pattern:** Linked List Traversal / Elementary Math
- **Time Complexity:** $O(\max(m, n))$
- **Space Complexity:** $O(\max(m, n))$ 
- **Verdict:** One-pass traversal using a dummy anchor node and carry-over logic.

## 🧠 The Logic "Aha!" Moment

The challenge isn't just adding numbers; it's handling the Linked List structure. Unlike an array, you can't just access `list[i]`.

**The Insight:** We treat this exactly like manual addition we learned in school. We move a "pointer" through both lists simultaneously. The "Aha!" was realizing that if one list ends, we don't stop—we just treat the missing digits as 0 until the other list (and any remaining carry) is also finished.

## 🚧 Trial & Error (My Process)

1. **Attempt 1** Struggled with the "final carry." If the last addition is $5 + 5$, you need to create an extra node for the `1.` Initially, my loop ended too early.
2. **Attempt 2** Switched from manual floor division and modulo (`total // 10`, `total % 10`) to the `divmod()` function to be more Pythonic and readable.
3. **Final Attempt (One-Pass):** Introduced the **Dummy Anchor node.** This solved the annoying "if result_head is None" check at the start of the loop.

---

## ⚠️ Edge Cases to Mention in Blog

- **Unequal Lengths:** Adding [9, 9] and [1]. The code must handle the "null" pointer for the shorter list without crashing.

- **The Final Carry:** Cases like `5 + 5` or `99 + 1` where the result is longer than both input lists. The while carry: condition in the loop handles this.

- **Zero Lists:** Adding [0] and [0]. The code should return [0], not an empty list or null.

## 💡 Real-World Analogy for Blog

**The Primary School Addition:** Imagine two people holding long chains of numbered blocks. To add them, they stand at the start of their chains and hand their blocks one by one to a third person (the "Adder"). If the Adder receives a 7 and a 5, they keep the 2 for the current block and put a "1" in their pocket (the carry) to add to the next pair of blocks handed to them.

## 🔗 Portfolio Connections

- **Related Patterns:** **Dummy Head Pattern** (used in Merge Two Sorted Lists), **Two-Pointer Traversal.**

- **Skills Demonstrated:** Pointer manipulation, handling "NoneType" objects in Python, and simulating mathematical processes.