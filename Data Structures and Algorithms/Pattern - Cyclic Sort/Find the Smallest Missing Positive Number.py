# Given an unsorted array containing numbers, find the smallest missing positive number in it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/R1GXQ071GQ0
# Leetcode https://leetcode.com/problems/first-missing-positive/
# Solution https://leetcode.com/problems/first-missing-positive/solution
# Time Complexity The time complexity of the above algorithm is O(n).
# Space Complexity The algorithm runs in constant space O(1).


def find_first_smallest_missing_positive(nums):
    i, n = 0, len(nums)
    while i < len(nums):
        j = nums[i]-1
        if nums[i]>0 and nums[i]<=n and nums[i] != nums[j]: # swap
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # The first number which is out-of-place is the smallest missing positive number
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return n+1


def main():
  print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
  print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
  print(find_first_smallest_missing_positive([3, 2, 5, 1]))


main()
