# Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/xV7wx4o8ymB
# Leetcode https://leetcode.com/problems/reorganize-string/
# Solution https://leetcode.com/problems/reorganize-string/solution/
# Time Complexity The time complexity of the above algorithm is O(N*logN) where ‘N’ is the number of characters in the input string.
# Space Complexity The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ characters in the HashMap.
from heapq import *
from collections import Counter, deque


def reorganize_string(str, k):
    if k <= 1:
        return str
    maxheap, result_str = [], []
    queue = deque()
    char_freq = Counter(str)
    # add all characters to the max heap
    for ele, freq in char_freq.items():
        heappush(maxheap, (-freq, ele))
    while maxheap:
        freq, char = heappop(maxheap)
        # append the current character to the result string
        result_str.append(char)
        # decrement the frequency and append to the queue
        queue.append((freq+1, char))
        # once the length of queue equals k, reinsert character back in maxheap
        if len(queue) == k:
            # add the previous entry back in the heap if its frequency is greater than zero
            freq, char = queue.popleft()
            if -freq > 0:
                heappush(maxheap, (freq, char))
    # if we were successful in appending all the characters to the result string, return it
    return "".join(result_str) if len(result_str) == len(str) else ""


def main():
    print("Reorganized string: " + reorganize_string("Programming", 3))
    print("Reorganized string: " + reorganize_string("mmpp", 2))
    print("Reorganized string: " + reorganize_string("aab", 2))
    print("Reorganized string: " + reorganize_string("aapa", 3))


main()
