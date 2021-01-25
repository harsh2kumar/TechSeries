# Problem Statement https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
from typing import List
import math


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0

        for i in nums:
            if (math.floor(math.log10(i))+1) % 2 == 0:
                count += 1
        return count


def main():
    obj = Solution()
    print(obj.findNumbers([1000]))


if __name__ == '__main__':
    main()
