# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier. Return the final order of the logs.
# Grokking
# Leetcode https://leetcode.com/problems/reorder-data-in-log-files/
# Solution https://leetcode.com/problems/reorder-data-in-log-files/solution/
# Let N be the number of logs in the list and M be the maximum length of a single log.
# Time Complexity O(M⋅N⋅logN)
# Space Complexity O(M⋅N)


from typing import List
import collections


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            # adding 0 in tuple enables letters to always be ordered before digits
            return (0, rest, _id) if rest[0].isalpha() else (1, )
        return sorted(logs, key=get_key)


sol = Solution()

print(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"], ": ", sol.reorderLogFiles(
    ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
print(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"], ": ", sol.reorderLogFiles(
    ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
