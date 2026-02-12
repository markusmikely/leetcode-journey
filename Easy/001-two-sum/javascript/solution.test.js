const twoSum = require('./solution');

describe('Two Sum - JavaScript', () => {
    test('Standard case: finds two numbers that add up to target', () => {
        expect(twoSum([2, 7, 11, 15], 9)).toEqual([0, 1]);
    });

    test('Handles negative numbers correctly', () => {
        expect(twoSum([-3, 4, 3, 90], 0)).toEqual([0, 2]);
    });

    test('Handles duplicate values in array', () => {
        expect(twoSum([3, 3], 6)).toEqual([0, 1]);
    });

    test('Returns an empty array when no solution is found', () => {
        expect(twoSum([1, 2, 3], 7)).toEqual([]);
    });
});