# Given an input string s, reverse the order of the words.
# Grokking
# Leetcode https://leetcode.com/problems/reverse-words-in-a-string/
# Solution https://leetcode.com/problems/reverse-words-in-a-string/solution/
# Time Complexity O(N), where N is a number of characters in the input string.
# Space Complexity O(N), to store the result of split by spaces.


from collections import deque


class Solution:

    # using inbuilt library functions
    def reverseWordsInbuilt(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    # using deque
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s)-1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        d, word = deque(), []

        # push woed by word in front of deque
        while left <= right:
            # add word in queue
            if s[left] == " " and word:
                d.appendleft("".join(word))
                word = []
            # create the word
            elif s[left] != " ":
                word.append(s[left])
            left += 1
        # append the last word
        d.appendleft("".join(word))

        # return reversed words
        return " ".join(d)


sol = Solution()
print("the sky is blue: ", sol.reverseWords("the sky is blue"))
print("  hello world  : ", sol.reverseWords("  hello world  "))
print("a good   example: ", sol.reverseWords("a good   example"))
