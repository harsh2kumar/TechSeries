# Given two version numbers, version1 and version2, compare them.
# Grokking
# Leetcode https://leetcode.com/problems/compare-version-numbers/
# Solution https://leetcode.com/problems/compare-version-numbers/solution/
# Time Complexity O(max(N,M)), where N and M are lengths of the input strings respectively. It's a one-pass solution.
# O(N+M+max(N,M)), where N and M are lengths of input strings for two-pass solution.
# Space Complexity O(max(N,M)) for one-pass solution. We still need some additional space to store a substring of the input string for integer conversion.
# In the worst case, the substring could be of the original string as well.
# O(N+M) to store arrays nums1 and nums2 for two-pass solution.


from typing import List
import collections


class Solution:
    def get_next_chunk(self, version, n, p):
        # if pointer has reached end of current version string
        # return 0
        if p > n-1:
            return 0, p
        # find the end of chunk
        p_end = p
        while p_end < n and version[p_end] != ".":
            p_end += 1
        # retrieve the chunk
        part = int(version[p:p_end]) if p_end < n else int(version[p:n])
        # find the beginning of next chunk
        p = p_end + 1
        return part, p

    def compareVersion_one_pass(self, version1: str, version2: str) -> int:
        n1, n2 = len(version1), len(version2)
        p1, p2 = 0, 0
        # compare versions
        while p1 < n1 or p2 < n2:
            i1, p1 = self.get_next_chunk(version1, n1, p1)
            i2, p2 = self.get_next_chunk(version2, n2, p2)

            if i1 != i2:
                return 1 if i1 > i2 else -1
        # the versions are equal
        return 0

    def compareVersion_two_pass(self, version1: str, version2: str) -> int:
        # split + parse, two pass
        num1 = version1.split(".")
        num2 = version2.split(".")
        n1, n2 = len(num1), len(num2)

        for i in range(max(n1, n2)):
            p = int(num1[i]) if i < n1 else 0
            q = int(num2[i]) if i < n2 else 0

            if p != q:
                return 1 if p > q else -1
        return 0


sol = Solution()
print("1.01", "1.001: ", sol.compareVersion_one_pass("1.01", "1.001"))
print("1.0", "1.0.0: ", sol.compareVersion_one_pass("1.0", "1.0.0"))
print("0.1", "1.1: ", sol.compareVersion_one_pass("0.1", "1.1"))

print("1.01", "1.001: ", sol.compareVersion_two_pass("1.01", "1.001"))
print("1.0", "1.0.0: ", sol.compareVersion_two_pass("1.0", "1.0.0"))
print("0.1", "1.1: ", sol.compareVersion_two_pass("0.1", "1.1"))
