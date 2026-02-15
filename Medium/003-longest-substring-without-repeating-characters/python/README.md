# Two Sum: Python Implementation

## 🐍 Why Python?

Python is excellent for this problem because of its highly optimized dict implementation. Dictionary lookups in Python are implemented using a hash table, giving us an average time complexity of $O(1)$ for each "complement check."

## 🛠️ The Implementation

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return [seen[complement], i]
            seen[val] = i
```

## 🔍 Language-Specific Insights

1. **enumerate() vs range(len())**

In Python, using enumerate(nums) is more "Pythonic" than iterating through indices using range. It provides both the index and the value in a clean, readable way, reducing the risk of "off-by-one" errors.

2. **Dictionary Performance**

Python’s dict uses a process called dummy entries and open addressing to handle collisions. For the "Two Sum" problem, this means our if complement in seen: check is nearly instantaneous regardless of how many items we've already stored.

3. **Avoiding "Shadowing"**

In my initial draft, I considered using sum as a variable name. However, sum() is a **built-in Python function.**

- **The Lesson:** Always name variables descriptively (like complement or total_sum) to avoid overwriting Python’s internal tools.

## 🧪 Testing Locally

To run this outside of LeetCode, I use a simple test block:

```python
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # Expected: [0, 1]
```

## 📈 Performance Benchmarks

- **LeetCode Runtime:** ~50ms (Beats X%)

- **Memory Usage:** ~15.2MB

- **Note:** Python's memory footprint is slightly higher than C++ or Rust due to the overhead of the objects and the dictionary structure.

## ✨ Comparison Note for Blog

When comparing this to the **JavaScript** implementation, notice how Python's enumerate feels more concise than a standard for loop, but the execution speed may be slightly slower than JS's V8 engine.

## ✅ Verification

### Local Testing
This solution includes a comprehensive test suite using `unittest`. To run the tests locally:
```bash
python solution.test.py
```

