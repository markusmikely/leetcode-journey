
# 002. Add Two Numbers

### 🔗 [Problem Link](https://leetcode.com/problems/add-two-numbers/)

## 💡 The Core Idea
Traverse both linked lists simultaneously in a single pass. The loop continues for the length of the longest list ($max(m, n)$) or as long as a **carry** value remains.

We utilize a **"Dummy Head" (Anchor Node)** pattern to gracefully build the resulting linked list without needing to handle the head initialization as a special case.

## ⚖️ The Trade-off
I chose a **Single-Pass** Iterative approach over converting the lists to integers and back. While converting to integers might seem simpler, it would fail for extremely large numbers that exceed standard integer limits (Overflow); the iterative pointer approach handles numbers of any length with $O(1)$ auxiliary space.

## ⚠️ Edge Cases
- **Unequal List Lengths:** One number has more digits than the other (e.g., $999 + 1$).
- **Final Carry:** The last addition results in a carry (e.g., $5 + 5$), requiring an extra node at the very end.
- **Empty/Zero Lists:** Input lists containing only a single 0 node.

## 👔 Real-World Analogy 
Think of two people holding long chains of numbered blocks. To add them, they stand at the start of their chains and hand their blocks one by one to a third person (the "Adder"). If the Adder receives a 7 and a 5, they keep the 2 for the current block and put a "1" in their pocket (the carry) to add to the next pair of blocks handed to them.

## 🚀 Complexity Analysis
- **Time:** $O(\max(m, n))$ — We visit each node in both lists at most once.
- **Space:** $O(\max(m, n))$ — The length of the new list is at most $max(m, n) + 1$. (Note: Auxiliary space is $O(1)$ if we don't count the space for the output list).

## 🛠️ Key Takeaways
- **Dummy Nodes:** A powerful pattern for simplifying linked list construction.
- **Elementary Math Simulation:** Replicating right-to-left addition using pointers.
- **Handling Unequal Lengths:** Using default values (0) when one list is shorter than the other.

## 📝 Blog Reference
*This solution is discussed in detail in my post: [How I Solved Add Two Numbers - Linked Lists](link-to-your-blog)*