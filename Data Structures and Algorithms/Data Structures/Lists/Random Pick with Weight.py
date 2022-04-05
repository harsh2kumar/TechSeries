# You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index. You need to implement the function pickIndex(),
# which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
# Grokking
# Leetcode https://leetcode.com/problems/random-pick-with-weight/
# Solution https://leetcode.com/problems/random-pick-with-weight/solution/
# Time Complexity The time complexity of O(log(N)). Intuitively the output is proportional to the number N of digits in the input.
# Space Complexity The space complexity is O(1), since the output is just a number.

from typing import List
import random
import bisect


class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sum = [w[0]]
        for i in range(1, len(w)):
            self.prefix_sum.append(self.prefix_sum[-1]+w[i])

    def pickIndex(self) -> int:
        random_int = random.randint(1, self.prefix_sum[-1])
        return bisect.bisect_left(self.prefix_sum, random_int)
        # return self.binary_search_ceil(self.prefix_sum, random_int)

    def binary_search_ceil(self, nums, ele) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end-start)//2
            if nums[mid] == ele:
                return mid
            elif nums[mid] > ele:
                end = mid-1
            else:
                start = mid+1
        return start

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


obj = Solution([1])
print("[1], pickIndex: ", obj.pickIndex())
obj = Solution([1, 3])
print("[1, 3], pickIndex, pickIndex, pickIndex, pickIndex, pickIndex: ", obj.pickIndex(
), obj.pickIndex(), obj.pickIndex(), obj.pickIndex(), obj.pickIndex())
