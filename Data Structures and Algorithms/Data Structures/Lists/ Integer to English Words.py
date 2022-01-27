# Convert a non-negative integer num to its English words representation.
# Grokking
# Leetcode https://leetcode.com/problems/integer-to-english-words/
# Solution https://leetcode.com/problems/integer-to-english-words/solution/
# Time Complexity The time complexity of O(N). Intuitively the output is proportional to the number N of digits in the input.
# Space Complexity The space complexity is O(1), since the output is just a string.

from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        # base case
        if num == 0:
            return "Zero"
        single_digit = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine"
        }

        teens = {
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety"
        }

        def parse_chunk(num: int) -> List[str]:
            # parse three digits
            result = []
            if num == 0:
                return result
            if num >= 100:
                result.extend([single_digit[num//100], "Hundred"])
                num %= 100
            if num >= 20:
                result.append(tens[num//10])
                num %= 10
            if num >= 10:
                result.append(teens[num])
                num %= 10
            elif num > 0:
                result.append(single_digit[num])
            return result

        result = []
        for name, size in [("Billion", 10**9), ("Million", 10**6), ("Thousand", 10**3)]:
            if size > num:
                continue
            result.extend(parse_chunk(num//size)+[name])
            num %= size
        return " ".join(result+(parse_chunk(num)))


sol = Solution()
print("123: ", sol.numberToWords(123))
print("12345: ", sol.numberToWords(12345))
print("1234567: ", sol.numberToWords(1234567))
print("123986876: ", sol.numberToWords(123986876))
print("999999990: ", sol.numberToWords(999999990))
print("999999999: ", sol.numberToWords(999999999))
print("0: ", sol.numberToWords(0))
