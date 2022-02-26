# You are given a list of songs where the ith song has a duration of time[i] seconds. Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.
# Grokking
# Leetcode https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# Solution https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/solution/
# Time Complexity O(n), when nn is the length of the input array, because we would visit each element in time once.
# Space Complexity O(1), because the size of the array remainders is fixed with 60.

from typing import List
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remainders = defaultdict(int)
        res = 0
        for t in time:
            if t % 60 == 0:  # check if a%60==0 & b%60==0
                res += remainders[0]
            else:  # check if a%60==0+b%60==0
                res += remainders[60-t % 60]
            remainders[t % 60] += 1
        return res


sol = Solution()
print("[30,20,150,100,40]: ",
      sol.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
print("[60,60,60]: ",
      sol.numPairsDivisibleBy60([60, 60, 60]))
