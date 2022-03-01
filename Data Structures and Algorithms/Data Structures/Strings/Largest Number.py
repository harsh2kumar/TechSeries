# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it. Since the result may be very large,
# so you need to return a string instead of an integer.
# Grokking
# Leetcode https://leetcode.com/problems/largest-number/
# Solution https://leetcode.com/problems/largest-number/solution/
# Time Complexity The time complexity of O(NlgN)
# Space Complexity The space complexity is O(N).

from typing import List


class CustomComp(str):
    # num1 = "30",  num2 = "3"
    # num1.num2 = 303 | num2.num1 = 330
    # we prefer num2.num1
    def __lt__(num1, num2):
        return num1+num2 > num2+num1


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        largest_num = "".join(sorted(nums, key=CustomComp))
        return "0" if largest_num[0] == "0" else largest_num


sol = Solution()
print("[10,2]: ", sol.largestNumber([10, 2]))
print("[3,30,34,5,9]: ", sol.largestNumber([3, 30, 34, 5, 9]))
