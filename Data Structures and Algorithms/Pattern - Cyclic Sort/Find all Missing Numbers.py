# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing.
# Find all those missing numbers.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/Y52qNM0ljWK
# Leetcode https://leetcode.com/problems/missing-number/
# Solution https://leetcode.com/problems/missing-number/solution
# Time Complexity The time complexity of the above algorithm is O(n).
# Space Complexity The algorithm runs in constant space O(1).


def find_missing_numbers(nums):
    i, n = 0, len(nums)
    missing_nums = []
    while i < n:
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i+1:
            missing_nums.append(i+1)
    return missing_nums


def main():
    print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))


main()
