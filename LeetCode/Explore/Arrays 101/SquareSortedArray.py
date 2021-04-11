from typing import List

class Solution:
    # trivial solution
    def sortedSquaresTrivial(self, nums: List[int]) -> List[int]:
        for index, value in enumerate(nums):
            nums[index] = value**2
        nums.sort()
        return nums

    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, j = 0, 0 # negative, positive numbers
        N = len(nums)

        while j<N and nums[j]<0:
            j += 1
        i = j-1

        while i>=0 and j<N:
            
        for index, value in enumerate(nums):
            nums[index] = value**2
        nums.sort()
        return nums

def main():
    obj = Solution()
    print(obj.sortedSquares([-4,-1,0,3,10]))


if __name__ == '__main__':
    main()

