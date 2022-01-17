# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# Grokking
# Leetcode https://leetcode.com/problems/move-zeroes/
# Solution https://leetcode.com/problems/move-zeroes/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(1).

class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1  # initialize sign to positive
        result = 0  # intitalize result to 0
        index = 0
        n = len(s)  # calculate length of given string

        INT_MAX = pow(2, 31)-1
        INT_MIN = -pow(2, 31)

        # skip all leading white spaces
        while index < n and s[index] == " ":
            index += 1

        # find whether number is positive or negative
        if index < n and s[index] == "+":
            sign = 1
            index += 1
        elif index < n and s[index] == "-":
            sign = -1
            index += 1

        # traverse next digits of input and stop if its not a digit
        # end of string is a non-digit char
        while index < n and s[index].isdigit():
            digit = int(s[index])
            # check overflow and underflow conditions
            if result > INT_MAX//10 or (result == INT_MAX//10 and digit > INT_MAX % 10):
                # if integer overflowed return 2^31-1, otherwise if underflowed return -2^31
                return INT_MAX if sign == 1 else INT_MIN
            # append current digit to result
            result = result*10 + digit
            index += 1

        # we have formed a valid number without any overflow/ underflow
        # return if after multiplying it with its sign
        return sign*result


sol = Solution()
print(sol.myAtoi("42"))
print(sol.myAtoi("   -42"))
print(sol.myAtoi("4193 with words"))
