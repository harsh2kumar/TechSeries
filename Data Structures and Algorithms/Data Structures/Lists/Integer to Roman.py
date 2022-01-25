# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. Given a roman numeral, convert it to an integer.
# Grokking
# Leetcode https://leetcode.com/problems/integer-to-roman/
# Solution https://leetcode.com/problems/integer-to-roman/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(1).

class Solution:
    def __init__(self):
        self.values = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90),
                       ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

    def intToRoman(self, num: int) -> str:
        roman_digits = []
        for symbol, val in self.values:
            if num == 0:
                break
            count, num = divmod(num, val)
            roman_digits.append(symbol*count)
        return "".join(roman_digits)


sol = Solution()
print("3: ", sol.intToRoman(3))
print("58: ", sol.intToRoman(58))
print("1994: ", sol.intToRoman(1994))
