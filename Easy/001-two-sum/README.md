
# 001. Two Sum

### 🔗 [Problem Link](https://leetcode.com/problems/two-sum/)

## 💡 The Core Idea
Instead of searching for two numbers, we search for the **complement** ($target - current$). We use a Hash Map to "remember" indices of numbers we've already passed.

## 🚀 Complexity Analysis
- **Time:** $O(n)$
- **Space:** $O(n)$

## 🛠️ Key Takeaways
- Trading space for time is a common optimization.
- Hash Maps provide $O(1)$ average lookup time.

## 📝 Blog Reference
*This solution is discussed in detail in my post: [How I Solved Two Sum](link-to-your-blog)*