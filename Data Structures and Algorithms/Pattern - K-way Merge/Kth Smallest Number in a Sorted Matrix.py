# Given an N * NN∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/x1NJVYKNvqz
# Leetcode https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Solution https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/
# Time Complexity First, we inserted at most ‘K’ or one element from each of the ‘N’ rows, which will take O(min(K, N)). Then we went through at 
# most ‘K’ elements in the matrix and remove/add one element in the heap in each step. As we can’t have more than ‘N’ elements in the heap in any condition, 
# therefore, the overall time complexity of the above algorithm will be O(min(K, N) + K*logN).
# Space Complexity The space complexity will be O(N) because, in the worst case, our min-heap will be storing one number from each of the ‘N’ rows.
from heapq import *


def find_Kth_smallest(matrix, k):
    minHeap = []

    # put the 1st element of each row in the min heap
    # we don't need to push more than 'k' elements in the heap
    for i in range(min(k, len(matrix))):
        heappush(minHeap, (matrix[i][0], 0, matrix[i]))

    # take the smallest(top) element form the min heap, if the running count is equal to k' return the number
    # if the row of the top element has more elements, add the next element to the heap
    numcount = 0
    while minHeap:
        ele, i, row = heappop(minHeap)
        numcount += 1
        if numcount == k:
            return ele
        if len(row) > i+1:
            heappush(minHeap, (row[i+1], i+1, row))
    return None


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()
