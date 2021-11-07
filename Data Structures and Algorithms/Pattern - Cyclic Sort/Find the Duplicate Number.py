# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times.
# Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3wEkKy6Pr9A
# Leetcode https://leetcode.com/problems/find-the-duplicate-number/
# Solution https://leetcode.com/problems/find-the-duplicate-number/solution
# Time Complexity The time complexity of the above algorithm is O(n).
# Space Complexity The algorithm runs in constant space O(1).


def find_duplicate(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i+1:
            j = nums[i]-1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                return nums[i]
        else:
            i += 1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()
