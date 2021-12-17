# Given a string, sort it based on the decreasing frequency of its characters.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/gxZz615BPPG
# Leetcode https://leetcode.com/problems/sort-characters-by-frequency/
# Solution https://leetcode.com/problems/sort-characters-by-frequency/solution/
# Time Complexity The time complexity of the above algorithm is O(D*logD) where ‘D’ is the number of distinct characters in the input string.
# This means, in the worst case, when all characters are unique the time complexity of the algorithm will be O(N*logN) where ‘N’ is the total number of
# characters in the string.
# Space Complexity The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.
from heapq import *
from collections import Counter


def sort_character_by_frequency(str):
    freq_str, maxheap = [], []
    # create frequency dictionary for given string
    str_dict = Counter(str)
    # add all elements in maxheap
    for ele, freq in str_dict.items():
        heappush(maxheap, (-freq, ele))
    # pop all elements from maxheap and populate characters of string
    while maxheap:
        freq, ele = heappop(maxheap)
        for _ in range(-freq):
            freq_str.append(ele)
    return "".join(freq_str)


def main():

    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
