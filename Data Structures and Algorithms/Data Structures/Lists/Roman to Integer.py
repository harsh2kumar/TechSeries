# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. Given a roman numeral, convert it to an integer.
# Grokking
# Leetcode https://leetcode.com/problems/roman-to-integer/
# Solution https://leetcode.com/problems/roman-to-integer/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(1).

class Solution:
    def __init__(self):
        self.values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            # improved pass
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

    # left to right pass; Compared to Right to Left pass,
    # this is slightly worse since we need to see the next character in advance
    # also the space req is slightly higher
    def romanToIntL2R(self, s: str) -> int:
        i, result = 0, 0

        while i < len(s):
            # if i+1<len(s) and self.values[s[i]]<self.values[s[i+1]]:
            #     result += self.values[s[i+1]]-self.values[s[i]]
            # improved pass
            # we added 6 more roman to decimal number conversions
            # to reduce comparisons
            if i+1 < len(s) and s[i:i+2] in self.values:
                result += self.values[s[i:i+2]]
                i += 2
            else:
                result += self.values[s[i]]
                i += 1

        return result

    # right to left pass
    # this is better because we just evaluate once
    def romanToIntR2L(self, s: str) -> int:
        i, result = len(s)-1, self.values[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if self.values[s[i]] < self.values[s[i+1]]:
                result -= self.values[s[i]]
            else:
                result += self.values[s[i]]
        return result


sol = Solution()
print("Left to Right evaluation")
print("III: ", sol.romanToIntL2R("III"))
print("LVIII: ", sol.romanToIntL2R("LVIII"))
print("MCMXCIV: ", sol.romanToIntL2R("MCMXCIV"))
print("Right to Left evaluation")
print("III: ", sol.romanToIntR2L("III"))
print("LVIII: ", sol.romanToIntR2L("LVIII"))
print("MCMXCIV: ", sol.romanToIntR2L("MCMXCIV"))
