# Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these
# substrings are grouped consecutively. Substrings that occur multiple times are counted the number of times they occur.
# Grokking
# Leetcode https://leetcode.com/problems/count-binary-substrings/
# Solution https://leetcode.com/problems/count-binary-substrings/solution/
# Time Complexity O(N), where N is the length of s. Every loop is through O(N) items with O(1) work inside the for-block.
# Space Complexity O(N), the space used by groups.


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # calculate the groups of same-character contiguous blocks
        # the first elment of s belongs in its own group
        # we keep on incrementing the length of first group until
        # we encounter a new group
        groups = [1]
        res = 0
        for i in range(1, len(s)):
            # start a new group if the previous element is different
            # from next element
            if s[i-1] != s[i]:
                groups.append(1)
            # increase length of current group
            else:
                groups[-1] += 1

        for i in range(1, len(groups)):
            res += min(groups[i-1], groups[i])

        return res


sol = Solution()
print("00110011", sol.countBinarySubstrings("00110011"))
print("10101", sol.countBinarySubstrings("10101"))
