# Two Sum: JavaScript Implementation

## 🟨 Why JavaScript?
JavaScript’s V8 engine is highly optimized for object property lookups. In this implementation, we use a standard JavaScript Object as a Hash Map, providing $O(1)$ average time complexity for insertions and lookups.

## 🛠️ The Implementation

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let seen = {}; // Hash Map to store {value: index}
    
    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        
        // Check if complement exists in our object
        if (seen[complement] !== undefined) {
            return [seen[complement], i];
        }
        
        // Store current value and its index
        seen[nums[i]] = i;
    }
    return [];
};
```

## 🧪 Testing Locally

This project uses **Jest** for verification. To run the tests:

```bash
# Install Jest (if not already installed)
npm install --save-dev jest

# Run the test
npx jest solution.test.js
```

## 📈 Performance Benchmarks

- **LeetCode Runtime:** ~0ms (Beats 100%)

- **Memory Usage:** ~56.72MB (Beats 14.06%)

- **Note:** JavaScript typically uses more memory than Python due to the way the V8 engine manages the heap and object properties.

## ✨ Comparison Note for Blog

Unlike Python's enumerate(), standard JavaScript requires a manual index increment in a for loop (unless using entries()). While slightly more verbose, the explicit control over the loop is very "JS-idiomatic.

## 🔍 Language-Specific Insights

1. **Object vs. Map (The Upgrade)**
   Initially, I used a plain Object (`{}`). I upgraded to `Map` for three key reasons:
   - **Key Types:** A `Map` can take any value as a key, whereas Objects restrict keys to Strings or Symbols.
   - **Performance:** `Map` performs better in scenarios involving frequent additions and removals.
   - **Size:** `Map` has a built-in `.size` property, making it easier to manage than counting keys in an Object.

2. **Avoiding the "Falsy Zero" Bug**
   By using `seen.has(complement)`, we completely avoid the risk of JavaScript treating index `0` as a "falsy" value. In a plain object, `if (seen[complement])` would fail if the stored index was `0`. `Map.has()` specifically checks for the existence of the key, not the truthiness of the value.