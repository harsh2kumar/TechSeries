# Given an input string s, reverse the order of the words.
# Grokking
# Leetcode https://leetcode.com/problems/reverse-words-in-a-string/
# Solution https://leetcode.com/problems/reverse-words-in-a-string/solution/
# Time Complexity O(N), where N is a number of characters in the input string.
# Space Complexity O(N), to store the result of split by spaces.


class Solution:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == ' ':
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == ' ':
            right -= 1

        # reduce multiple spaces to single one
        output = []
        while left <= right:
            if s[left] != ' ':
                output.append(s[left])
            elif output[-1] != ' ':
                output.append(s[left])
            left += 1

        return output

    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # go to the end of the word
            while end < n and l[end] != ' ':
                end += 1
            # reverse the word
            self.reverse(l, start, end - 1)
            # move to the next word
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:
        # converst string to char array
        # and trim spaces at the same time
        l = self.trim_spaces(s)

        # reverse the whole string
        self.reverse(l, 0, len(l) - 1)

        # reverse each word
        self.reverse_each_word(l)

        return ''.join(l)


sol = Solution()
print("the sky is blue: ", sol.reverseWords("the sky is blue"))
print("  hello world  : ", sol.reverseWords("  hello world  "))
print("a good   example: ", sol.reverseWords("a good   example"))
