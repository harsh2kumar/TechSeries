# Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/JPGWDNRx3w2
# Leetcode https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# Solution https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/solution/
# Time Complexity Since, at most, we’ll be going through all the elements of all the arrays and will remove/add one element in the heap in each step, the time
# complexity of the above algorithm will be O(N*logM) where ‘N’ is the total number of elements in all the ‘M’ input arrays.
# Space Complexity The space complexity will be O(M) because, at any time, our min-heap will be store one number from all the ‘M’ input arrays.
from heapq import *


def find_smallest_range(nums):
    range_start, range_end = 0, float('inf')
    maxnum = -float('inf')
    minheap = []

    # put the 1st element of each row in the min heap
    # maxnum will always contain smallest maximums of the M arrays as they are sorted in ascneding order
    for sublist in nums:
        heappush(minheap, (sublist[0], 0, sublist))
        maxnum = max(maxnum, sublist[0])
    # take the smallest(top) element form the min heap, if it gives us smaller range, update the ranges
    # if the array of the top element has more elements, insert the next element in the heap
    while len(minheap) == len(nums):
        ele, i, sublist = heappop(minheap)
        if range_end-range_start > maxnum-ele:
            range_start = ele
            range_end = maxnum
        if len(sublist) > i+1:
            # insert the next element in the heap
            # calculate the new maximum
            heappush(minheap, (sublist[i+1], i+1, sublist))
            maxnum = max(maxnum, sublist[i+1])
    return [range_start, range_end]


def main():
    print("Smallest range is: " +
          str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]])))


main()
