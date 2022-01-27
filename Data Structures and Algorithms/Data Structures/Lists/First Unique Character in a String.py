# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Grokking
# Leetcode https://leetcode.com/problems/first-unique-character-in-a-string/
# Solution https://leetcode.com/problems/first-unique-character-in-a-string/solution/
# Time Complexity O(N) since we go through the string of length N two times.
# Space Complexity O(1) because English alphabet contains 26 letters.

from typing import List
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = collections.Counter(s)
        for i in range(len(s)):
            if char_count[s[i]] == 1:
                return i
        return -1


sol = Solution()
print("leetcode", sol.firstUniqChar("leetcode"))
print("loveleetcode", sol.firstUniqChar("loveleetcode"))
print("aabb", sol.firstUniqChar("aabb"))
