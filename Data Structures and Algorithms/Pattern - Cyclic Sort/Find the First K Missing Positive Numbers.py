# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/q2LA7G0ANX0
# Leetcode
# Solution
# Time Complexity The time complexity of the above algorithm is O(n + k), as the last two for loops will run for O(n) and O(k) times respectively.
# Space Complexity The algorithm needs O(k) space to store the extraNumbers.


def find_first_k_missing_positive(nums, k):
    i, n = 0, len(nums)
    missing_nums, extra_nums = [], set()
    while i < len(nums):
        j = nums[i]-1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:  # swap
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    # prepare a list of all missing_nums and extra_nums
    # we won't append extra_nums to missing_nums
    for i in range(len(nums)):
        if len(missing_nums) < k:
            if nums[i] != i+1:
                missing_nums.append(i+1)
                extra_nums.add(nums[i])

    # add more nums to missing_nums if its length is less than k
    i = 1
    while len(missing_nums) < k:
        num = i+n
        if num not in extra_nums:
            missing_nums.append(num)
        i += 1
    return missing_nums


def main():
    print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
    print(find_first_k_missing_positive([2, 3, 4], 3))
    print(find_first_k_missing_positive([-2, -3, 4], 2))


main()
