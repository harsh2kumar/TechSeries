# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Grokking 
# Leetcode https://leetcode.com/problems/move-zeroes/
# Solution https://leetcode.com/problems/move-zeroes/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(1).

def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) <= 1:
        return
    # start from end, go towards beginning
    i, last_non_zero_index = 0, 0
    while i < len(nums):
        # if you find a non-zero number, swap it with last_non_zero index
        # since we want to maintain order of elements
        # the best position for a non-zero num is the current index
        if nums[i] != 0:
            nums[i], nums[last_non_zero_index] = nums[last_non_zero_index], nums[i]
            last_non_zero_index += 1
        i += 1
