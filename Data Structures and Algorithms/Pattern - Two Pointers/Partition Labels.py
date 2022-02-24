# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. Note that the partition is
# done so that after concatenating all the parts in order, the resultant string should be s. Return a list of integers representing the size of these parts.
# Grokking
# Leetcode https://leetcode.com/problems/partition-labels/
# Solution https://leetcode.com/problems/partition-labels//solution/
# Time Complexity The above algorithm’s time complexity will be O(N) where N is the length of given string.
# Space Complexity The algorithm runs in constant space O(1).


from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {c: i for i, c in enumerate(s)}
        # anchor and j represent start and end of current partition
        j = anchor = 0
        res = []
        for i, c in enumerate(s):
            j = max(j, last_pos[c])
            if i == j:
                # append length of current partition
                res.append(i-anchor+1)
                anchor = i+1
        return res


sol = Solution()
print("ababcbacadefegdehijhklij", sol.partitionLabels("ababcbacadefegdehijhklij"))
print("eccbbbbdec", sol.partitionLabels("eccbbbbdec"))
