# Problem Statement https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count, count = -1, 0
        
        for i in nums:
            if i != 1:
                max_count = max(max_count, count)
                count = 0
            else:
                count += 1
        return max(max_count, count)           