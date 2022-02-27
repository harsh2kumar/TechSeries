# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.
# Grokking
# Leetcode https://leetcode.com/problems/flip-string-to-monotone-increasing/
# Solution https://leetcode.com/problems/flip-string-to-monotone-increasing/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(1).


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # From Comment
        # just for those who have trouble understanding intuition. Basically we go through string and found out how many 1 before index need to be flipped to 0 and how many 0 after index need to be flipped to 1. add them up and get min for result
        ones, zeros = 0, 0
        # Evidently, it comes down to a question of knowing, for each candidate half: how many ones are in the left half, and how many zeros are in the right half.
        for char in s:
            if char == '1':
                ones += 1
            else:
                zeros += 1
            # print("ones: ", ones, "zeros: ", zeros)
            # calculate minimum number of flips required till current index
            # how many 1s need to be flipped to 0 before current index (left half)
            flip = min(ones, zeros)
            # how many 0s need to be filpped to 1 (right half)
            zeros = min(flip, zeros)
            # print("flip to 1:", flip, "flip zeros: ", zeros)
        return flip

    def minFlipsMonoIncrEasy(self, s: str) -> int:
        # num of zeros to flip to 1
        # num of 1 to flip to 0
        zeros, ones = s.count("0"), 0
        # at the very minimum result would be equal to number zeros
        result = zeros
        
        for char in s:
            if char == '0':
                zeros -= 1
                
            else:
                ones += 1
            result = min(result, zeros+ones)
        return result

sol = Solution()
print("00110: ", sol.minFlipsMonoIncr("00110"))
print("010110: ", sol.minFlipsMonoIncr("010110"))
print("00011000: ", sol.minFlipsMonoIncr("00011000"))

print("00110: ", sol.minFlipsMonoIncrEasy("00110"))
print("010110: ", sol.minFlipsMonoIncrEasy("010110"))
print("00011000: ", sol.minFlipsMonoIncrEasy("00011000"))
