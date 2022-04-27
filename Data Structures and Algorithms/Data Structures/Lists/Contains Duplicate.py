# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Grokking
# Leetcode https://leetcode.com/problems/contains-duplicate/
# Solution https://leetcode.com/problems/contains-duplicate/solution/
# Time Complexity  O(n). We do contains() and add() for n times and each operation takes constant time.
# Space Complexity O(n). The space used by a hash table is linear with the number of elements in it.


from typing import List
import collections


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create a set using all numbers and returning false if length differes
        # hashset = set(nums)
        # if len(hashset) != len(nums):
        #     return True
        # return False

        # return false if an element is already present in our set
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False


sol = Solution()

print("[1,2,3,1]: ", sol.containsDuplicate([1, 2, 3, 1]))
print("[1,2,3,4]: ", sol.containsDuplicate([1, 2, 3, 4]))
print("[1,1,1,3,3,4,3,2,4,2]: ", sol.containsDuplicate(
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
