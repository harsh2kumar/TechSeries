# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Grokking
# Leetcode https://leetcode.com/problems/group-anagrams/
# Solution https://leetcode.com/problems/group-anagrams/solution/
# Time Complexity The time complexity of O(N.KlogK) or O(N.K), for sorted character key or count of character based key where N is total number words and
# K is length of each word.
# Space Complexity The space complexity is O(N.K) required for storing all words.

from typing import List
import collections


class Solution:
    def groupAnagrams_SS(self, strs: List[str]) -> List[List[str]]:
        # categorize by sorted string
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

    def groupAnagrams_C(self, strs: List[str]) -> List[List[str]]:
        # categorize by count
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


sol = Solution()
print(str(["eat", "tea", "tan", "ate", "nat", "bat"]),
      sol.groupAnagrams_SS(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(str([""]), sol.groupAnagrams_SS([""]))
print(str(["a"]), sol.groupAnagrams_SS(["a"]))

print(str(["eat", "tea", "tan", "ate", "nat", "bat"]),
      sol.groupAnagrams_C(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(str([""]), sol.groupAnagrams_C([""]))
print(str(["a"]), sol.groupAnagrams_C(["a"]))
