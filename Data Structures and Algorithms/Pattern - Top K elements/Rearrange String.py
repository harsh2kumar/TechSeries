# Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/xV7wx4o8ymB
# Leetcode https://leetcode.com/problems/reorganize-string/
# Solution https://leetcode.com/problems/reorganize-string/solution/
# Time Complexity The time complexity of the above algorithm is O(N*logN) where ‘N’ is the number of characters in the input string.
# Space Complexity The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.
from heapq import *
from collections import Counter


def rearrange_string(str):
    maxheap, result_str = [], []
    char_freq = Counter(str)
    # add all characters to the max heap
    for ele, freq in char_freq.items():
        heappush(maxheap, (-freq, ele))
    prev_char, prev_freq = None, 0
    while maxheap:
        freq, char = heappop(maxheap)
        # add the previous entry back in the heap if its frequency is greater than zero
        if prev_char and -prev_freq > 0:
            heappush(maxheap, (prev_freq, prev_char))
        # append the current character to the result string and decrement its count
        result_str.append(char)
        prev_char = char
        prev_freq = freq+1  # decrement the frequency
    # if we were successful in appending all the characters to the result string, return it
    return "".join(result_str) if len(result_str) == len(str) else ""


def main():
    print("Rearranged string:  " + rearrange_string("aappp"))
    print("Rearranged string:  " + rearrange_string("Programming"))
    print("Rearranged string:  " + rearrange_string("aapa"))


main()
