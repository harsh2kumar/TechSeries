# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/myAqDMyRXn3
# Leetcode https://leetcode.com/problems/merge-k-sorted-lists/
# Solution https://leetcode.com/problems/merge-k-sorted-lists/solution/
# Time Complexity Since we’ll be going through at most ‘K’ elements among all the arrays, and we will remove/add one element in the heap in each step,
# the time complexity of the above algorithm will be O(K*logM) where ‘M’ is the total number of input arrays.
# Space Complexity The space complexity will be O(M) because, at any time, our min-heap will be storing one number from all the ‘M’ input arrays.
from heapq import *


def find_Kth_smallest(lists, k):
    minheap = []
    numcount = 0

    # put the 1st element of each list in the min heap
    for sublist in lists:
        heappush(minheap, (sublist[0], 0, sublist))
    # take the smallest(top) element form the min heap, if the running count is equal to k return the number
    while minheap:
        ele, i, sublist = heappop(minheap)
        numcount += 1
        if numcount == k:
            return ele
        # if the array of the top element has more elements, add the next element to the heap
        if len(sublist) > i+1:
            heappush(minheap, (sublist[i+1], i+1, sublist))


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()
