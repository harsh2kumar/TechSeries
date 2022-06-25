# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive. A subarray of an array is a
# consecutive sequence of zero or more values taken out of that array. Return the maximum length of a subarray with positive product.
# Grokking
# Leetcode https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
# Solution https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/solution/
# Time Complexity O(n). Only a single pass is needed.
# Space Complexity O(n). We maintain a DP array for pos and neg. We caould compress it to O(1) as well as we only need values from the last iteration.

from typing import List


class Solution:
    def getMaxLenBrute(self, nums: List[int]) -> int:

        # TLE
        # brute force with pruning
        result = 0

        for i in range(len(nums)):
            # pruning step
            if len(nums)-i <= result:
                return result
            # prune
            if nums[i] != 0:
                negatives = 0 if nums[i] > 0 else 1
                result = max(result, 1 if nums[i] > 0 else 0)
                for j in range(i+1, len(nums)):
                    if nums[j] < 0:
                        negatives += 1
                    elif nums[j] == 0:
                        break
                    if negatives % 2 == 0:
                        result = max(result, j-i+1)

        return result

    def getMaxLen(self, nums: List[int]) -> int:
        # DP solution
        # initializing with 0, means that we already handle the case
        # wher we encounter a 0 within the subarray as the max value is reset
        pos = [0]*len(nums)  # length of longest subarray with postive product
        neg = [0]*len(nums)  # length of longest subarray with negative product

        # initilize first element of neg and pos as we start with index 1
        if nums[0] > 0:
            pos[0] = 1
        elif nums[0] < 0:
            neg[0] = 1
        # we want the max postive product
        ans = pos[0]

        for i in range(1, len(nums)):
            # positive number case
            if nums[i] > 0:
                pos[i] = pos[i-1] + 1
                # if a negative number was seen previously
                # negative product will be maintained and max length of that subarray is
                # prev max length + 1
                if neg[i-1] > 0:
                    neg[i] = neg[i-1] + 1
            # negative number case
            elif nums[i] < 0:
                # if a negative number was seen previously
                # negative product will change to positive product and max length of that subarray is
                # prev negative max length + 1
                if neg[i-1] > 0:
                    pos[i] = neg[i-1] + 1
                neg[i] = pos[i-1] + 1
            ans = max(ans, pos[i])
        return ans

    def getMaxLenSpaceOptimized(self, nums: List[int]) -> int:
        # DP solution
        # initializing with 0, means that we already handle the case
        # wher we encounter a 0 within the subarray as the max value is reset
        pos = 0  # length of longest subarray with postive product
        neg = 0  # length of longest subarray with negative product

        # initilize first element of neg and pos as we start with index 1
        if nums[0] > 0:
            pos = 1
        elif nums[0] < 0:
            neg = 1
        # we want the max postive product
        ans = pos

        for i in range(1, len(nums)):
            pos2 = neg2 = 0
            # positive number case
            if nums[i] > 0:
                pos2 = pos + 1
                # if a negative number was seen previously
                # negative product will be maintained and max length of that subarray is
                # prev max length + 1
                if neg > 0:
                    neg2 = neg + 1
            # negative number case
            elif nums[i] < 0:
                # if a negative number was seen previously
                # negative product will change to positive product and max length of that subarray is
                # prev negative max length + 1
                if neg > 0:
                    pos2 = neg + 1
                neg2 = pos + 1
            pos = pos2
            neg = neg2
            ans = max(ans, pos)
        return ans


sol = Solution()
print("Brute-Force")
print(sol.getMaxLenBrute([1, -2, -3, 4]))
print(sol.getMaxLenBrute([0, 1, -2, -3, -4]))
print(sol.getMaxLenBrute([-1, -2, -3, 0, 1]))
print("Single-Pass")
print(sol.getMaxLen([1, -2, -3, 4]))
print(sol.getMaxLen([0, 1, -2, -3, -4]))
print(sol.getMaxLen([-1, -2, -3, 0, 1]))
