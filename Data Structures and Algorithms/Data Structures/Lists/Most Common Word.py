# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned.
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.
# Grokking
# Leetcode https://leetcode.com/problems/most-common-word/
# Solution https://leetcode.com/problems/most-common-word/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(1).

import collections
from typing import List
import operator


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        normalized_str = "".join(
            [c.lower() if c.isalnum() else " " for c in paragraph])

        words = normalized_str.split()

        word_count = collections.defaultdict(int)
        banned_words = set(banned)

        for word in words:
            if word not in banned_words:
                word_count[word] += 1
        return max(word_count.items(), key=operator.itemgetter(1))[0]


sol = Solution()


print(sol.mostCommonWord(
    "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(sol.mostCommonWord("a.", []))
