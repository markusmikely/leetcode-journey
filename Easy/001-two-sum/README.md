
# 001. Two Sum

### 🔗 [Problem Link](https://leetcode.com/problems/two-sum/)

## 💡 The Core Idea
Instead of searching for two numbers using nested loops, we iterate through the array once and calculate the **complement**NOTE -  ($target - current$). We use a Hash Map to "remember" the numbers we've seen so far, allowing us to find the complement in $O(1)$ time.

## ⚖️ The Trade-off
I chose the **One-Pass Hash Map** over the Brute Force ($O(n^2)$) approach. This is a classic "space-for-time" trade-off; by using $O(n)$ extra memory to store a dictionary, we drastically reduce the execution time from quadratic to linear, which is essential for large datasets.

## ⚠️ Edge Cases
- **Duplicate Values:** The target is 6 and the array is [3, 3]. The map must correctly store and retrieve the indices without overwriting the first occurrence before it's checked.

- **Negative Numbers:** The logic must hold true when the target or array elements are negative (e.g., target is -5, current is 2, complement is -7).

- **First Two Elements:** The solution must be able to return the very first two indices if they satisfy the target.

## 👔 Real-World Analogy
Think of a **"Missing Person"** list. As you walk through a crowd (the array), you look at each person's face. You check your list to see if anyone is looking for the person currently standing in front of you. If not, you write down that person's name and where you saw them (index) so the next person in the crowd can check against it.

## 🚀 Complexity Analysis
- **Time:** $O(n)$
- **Space:** $O(n)$

## 🛠️ Key Takeaways
- **One-Pass vs. Two-Pass:** Understanding that we can build the map while searching, which naturally prevents using the same element twice.
- **Hash Map Efficiency:** Leveraging $O(1)$ average lookups to eliminate nested loops.

## 📝 Blog Reference
*This solution is discussed in detail in my post: [How I Solved Two Sum](link-to-your-blog)*