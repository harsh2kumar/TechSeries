# We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence.
# Write a function to sort the objects in-place on their creation sequence number in O(n) and without using any extra space.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B8qXVqVwDKY
# Leetcode
# Solution
# Time Complexity The time complexity of the above algorithm is O(n).
# Space Complexity The algorithm runs in constant space O(1).


def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    return nums


def main():
    print(cyclic_sort([3, 1, 5, 4, 2]))
    print(cyclic_sort([2, 6, 4, 3, 1, 5]))
    print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()
