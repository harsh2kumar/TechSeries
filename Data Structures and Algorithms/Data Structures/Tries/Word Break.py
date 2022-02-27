# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Grokking
# Leetcode https://leetcode.com/problems/word-break/
# Solution https://leetcode.com/problems/word-break/solution/
# Time Complexity O(n^3). Size of recursion tree can go up to n^2.
# Space Complexity O(n). The depth of recursion tree can go up to n.

from functools import lru_cache
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(maxsize=4096)
        def wordBreakRec(s, word_dict, start):
            if start == len(s):
                return True
            for end in range(start+1, len(s)+1):
                if s[start:end] in word_dict and wordBreakRec(s, word_dict, end):
                    return True
            return False
        return wordBreakRec(s, frozenset(wordDict), 0)


sol = Solution()
print('"leetcode", ["leet","code"]: ',
      sol.wordBreak("leetcode", ["leet", "code"]))
print('"applepenapple", ["apple","pen"]: ',
      sol.wordBreak("applepenapple", ["apple", "pen"]))
print('"catsandog", ["cats","dog","sand","and","cat"]: ', sol.wordBreak(
    "catsandog", ["cats", "dog", "sand", "and", "cat"]))
