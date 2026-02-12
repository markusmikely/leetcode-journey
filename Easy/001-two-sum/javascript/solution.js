/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let seen = new Map(); // Using Map instead of a plain Object
    for(let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        // Map.has() is the explicit way to check for existence
        if (seen.has(complement)) {
            return [seen.get(complement), i];
        }
        // Map.set() stores the value and index
        seen.set(nums[i], i);
    }
    return []
};

module.exports = twoSum;