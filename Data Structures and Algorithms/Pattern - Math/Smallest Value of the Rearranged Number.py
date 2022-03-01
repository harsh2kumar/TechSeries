# You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros. Return the rearranged number
# with minimal value. Note: that the sign of the number does not change after rearranging the digits.
# Grokking
# Leetcode https://leetcode.com/problems/smallest-value-of-the-rearranged-number/
# Solution https://leetcode.com/problems/smallest-value-of-the-rearranged-number/solution/
# Time Complexity The time complexity of O(NlgN).
# Space Complexity The space complexity is O(N).

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return num
        is_negative = num < 0
        num = abs(num)
        num = list(str(num))
        # to get smallest negative number, sort all digits in dessending order and prefix "-" sign
        if is_negative:
            return -int("".join(sorted(num, reverse=True)))

        # for positive number, find the min digit which isn't zero
        min_digit = min(d for d in num if d != "0")
        num.remove(str(min_digit))
        return int(min_digit+"".join(sorted(num)))


sol = Solution()
print("310: ", sol.smallestNumber(310))
print("-7605: ", sol.smallestNumber(-7605))
