
# 002. Add Two Numbers

### 🔗 [Problem Link](https://leetcode.com/problems/add-two-numbers/)

## 💡 The Core Idea
Traverse both linked lists simultaneously in a single pass. The loop continues for the length of the longest list ($max(m, n)$) or as long as a **carry** value remains.

We utilize a **"Dummy Head" (Anchor Node)** pattern to gracefully build the resulting linked list without needing to handle the head initialization as a special case.

## 🚀 Complexity Analysis
- **Time:** $O(\max(m, n))$ — We visit each node in both lists at most once.
- **Space:** $O(\max(m, n))$ — The length of the new list is at most $max(m, n) + 1$. (Note: Auxiliary space is $O(1)$ if we don't count the space for the output list).

## 🛠️ Key Takeaways
- **Dummy Nodes:** A powerful pattern for simplifying linked list construction.
- **Elementary Math Simulation:** Replicating right-to-left addition using pointers.
- **Handling Unequal Lengths:** Using default values (0) when one list is shorter than the other.

## 📝 Blog Reference
*This solution is discussed in detail in my post: [How I Solved Add Two Numbers - Linked Lists](link-to-your-blog)*