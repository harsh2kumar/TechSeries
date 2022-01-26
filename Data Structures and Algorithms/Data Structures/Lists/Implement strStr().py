# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Grokking
# Leetcode https://leetcode.com/problems/implement-strstr/
# Solution https://leetcode.com/problems/implement-strstr/solution/
# Time Complexity The time complexity of O(M.N), where M and N are the lengths of haystack and needle.
# Space Complexity The space complexity is O(1).

from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)
        if length == 0:
            return 0
        for i in range(len(haystack)-length+1):
            if haystack[i:i+length] == needle:
                return i
        return -1


sol = Solution()
print("hello, ll", sol.strStr("hello", "ll"))
print("aaaaa, bba", sol.strStr("aaaaa", "bba"))
print(", ", sol.strStr("", ""))
print("a, a", sol.strStr("a", "a"))
