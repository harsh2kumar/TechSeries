class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_window = -1
        left, right = 0, 0
        
        for index, n in enumerate(nums):
            if n == 1:
                left = index
                right = index
                break
        
        for i in range(index, len(nums)):
            if nums[i] != 1:
                right = i-1
                if current_window < (right-left+1):
                    current_window = (right-left+1)
                right = i
                left = right
            