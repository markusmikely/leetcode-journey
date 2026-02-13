# Add Two Numbers: JavaScript Implementation

## 🟨 Why JavaScript?
In this implementation, JavaScript’s behavior with numbers and object references is key:

- **Float Precision:** Unlike Python, JS treats all numbers as 64-bit floats. We use Math.floor() to explicitly handle "integer division," ensuring our carry remains a clean integer rather than a decimal.

- **Reference-Based Objects:** The ListNode class leverages JavaScript's pointer-like behavior. By updating tail.next, we are modifying the original object in memory, allowing us to build a complex chain while only keeping track of a single anchor reference.

- **Automatic Garbage Collection:** As we traverse l1 and l2, we don't need to manually deallocate the nodes we've already "passed." The V8 engine identifies when a node is no longer reachable and frees that memory for us.

## 🛠️ The Implementation

```javascript
class ListNode {
    constructor(val, next) {
        this.val = (val === undefined ? 0 : val);
        this.next = (next === undefined ? null : next);
    }
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    // Dummy head; to gracefully handle null values
    let anchor = new ListNode(0)
    let curr = anchor;
    let carry = 0; // will hold any values that need to carry over to the next digit being added
    
    // If l1 or l2 are not null, or carry > 0 we still ave vals to add
    while(l1 !== null || l2 !== null || carry > 0) {
        const val1 = l1 ? l1.val : 0
        const val2 = l2 ? l2.val : 0
        const total = val1 + val2 + carry
        carry = Math.floor(total / 10) // the 10s to carry over
        const out = total % 10 // the remainder after removing the 10

        curr.next = new ListNode(out) // create a new node
        curr = curr.next

        l1 = l1 ? l1.next : null
        l2 = l2 ? l2.next : null
    }
    return anchor.next
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

- **LeetCode Runtime:** ~60ms

- **Memory Usage:** ~42.5MB

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