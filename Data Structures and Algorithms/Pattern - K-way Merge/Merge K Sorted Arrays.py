# Given a list of ‘M’ sorted arrays, merge them into one sorted list.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/myAqDMyRXn3#Similar-Problems-
# Leetcode
# Solution
# Time Complexity Since we’ll be going through all the elements of all arrays and will be removing/adding one element to the heap in each step, the time complexity
# of the above algorithm will be O(K*logM), where ‘K’ is the total number of elements in all the ‘M’ input arrays.
# Space Complexity The space complexity will be O(M) because, at any time, our min-heap will be storing one number from all the ‘M’ input arrays.
from heapq import *


def merge_arrays(lists):
    result, minheap = [], []
    # put the 1st element of each list in the min heap
    for sublist in lists:
        heappush(minheap, (sublist[0], 0, sublist))
    result_head, result_tail = None, None
    # take the smallest(top) element form the min heap
    while minheap:
        ele, i, sublist = heappop(minheap)
        result.append(ele)
        # if the array of the top element has more elements, add the next element to the heap
        if len(sublist) > (i+1):
            heappush(minheap, (sublist[i+1], i+1, sublist))
    return result


def main():
    print("Here are the elements form the merged list: " +
          str(merge_arrays([[2, 6, 8], [3, 6, 7], [1, 3, 4]])))


main()
