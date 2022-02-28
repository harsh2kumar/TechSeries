# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray. Return the sum of
# all subarray ranges of nums. A subarray is a contiguous non-empty sequence of elements within an array.
# Grokking
# Leetcode https://leetcode.com/problems/sum-of-subarray-ranges/
# Solution https://leetcode.com/problems/sum-of-subarray-ranges/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(N).

from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # we need to find the difference between the max and min value in all subarrays
        result = 0
        if not nums:
            return result
        # monotonically increasing stack to find the the minimum value of all subarrays
        min_mono_stack = []  # pair(index, num)
        # monotonically decreasing stack to find the maximum value in all subarrays
        max_mono_stack = []  # pair(index, num)
        nums.append(0)  # to construct subarray using the last element
        for i, n in enumerate(nums):
            while min_mono_stack and (n < min_mono_stack[-1][1] or i == len(nums)-1):
                index, num = min_mono_stack.pop()
                if min_mono_stack:
                    left_length = index - min_mono_stack[-1][0]
                else:  # this is the only element in stack
                    left_length = index + 1  # next smaller element than all the previous elements
                right_length = i - index
                result -= left_length*right_length*num
            min_mono_stack.append((i, n))
            while max_mono_stack and (n > max_mono_stack[-1][1] or i == len(nums)-1):
                index, num = max_mono_stack.pop()
                if max_mono_stack:
                    left_length = index - max_mono_stack[-1][0]
                else:  # this is the only element in stack
                    left_length = index + 1  # next bigger element than all the previous elements
                right_length = i - index
                result += left_length*right_length*num
            max_mono_stack.append((i, n))
        return result


sol = Solution()
print("[1,2,3]: ", sol.subArrayRanges([1, 2, 3]))
print("[1,3,3]: ", sol.subArrayRanges([1, 3, 3]))
print("[4,-2,-3,4,1]: ", sol.subArrayRanges([4, -2, -3, 4, 1]))
