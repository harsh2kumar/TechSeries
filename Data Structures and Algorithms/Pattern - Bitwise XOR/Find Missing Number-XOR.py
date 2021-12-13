# Given an array of n−1 integers in the range from 1 to n, find the one number that is missing from the array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RLPGq6Vx0YY
# Leetcode https://leetcode.com/problems/missing-number/
# Solution https://leetcode.com/problems/missing-number/solution/
# Time Complexity Since, wThe time complexity of our algorithm will be O(N), where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def find_missing_number(nums):
    n = len(nums)+1
    x1 = 1

    for i in range(2, n+1):
        x1 ^= i
    x2 = nums[0]
    for j in range(1, n-1):
        x2 ^= nums[j]
    return x1 ^ x2


def main():
    arr = [1, 5, 2, 6, 4]
    print('Missing number is:' + str(find_missing_number(arr)))


main()
