# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad. You are given an API
# bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of
# calls to the API.
# Grokking
# Leetcode https://leetcode.com/problems/first-bad-version/
# Solution https://leetcode.com/problems/first-bad-version/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
bad_num = 0


def isBadVersion(num: int) -> bool:
    if num == bad_num:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        while start < end:
            mid = start + (end-start)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid+1

        return start


sol = Solution()
bad_num = 4
print(sol.firstBadVersion(5))
bad_num = 1
print(sol.firstBadVersion(1))
