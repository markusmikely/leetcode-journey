/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let pairs = {}
    for(let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];
        if(pairs[complement] !== undefined) {
            return [pairs[complement], i]
        } else {
            const value = nums[i]
            pairs[value] = i
        }
    }
    return []
};

module.exports = twoSum;