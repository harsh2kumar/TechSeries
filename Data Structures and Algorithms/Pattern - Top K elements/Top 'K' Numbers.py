# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RM535yM9DW0
# Leetcode https://leetcode.com/problems/kth-largest-element-in-an-array/
# Solution https://leetcode.com/problems/kth-largest-element-in-an-array/solution/
# Time Complexity As discussed above, the time complexity of this algorithm is O(K*logK+(N-K)*logK), which is asymptotically equal to O(N*logK)
# Space Complexity The space complexity will be O(K) since we need to store the top ‘K’ numbers in the heap.
from heapq import *


def find_k_largest_numbers(nums, k):
    minheap = []
    # put first 'K' numbers in the min heap
    for i in range(k):
        heappush(minheap, nums[i])
    # go through the remaining numbers of the array, if the number from the array is bigger than the
    # top(smallest) number of the min-heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if nums[i] > minheap[0]:
            heappop(minheap)
            heappush(minheap, nums[i])
    # the heap has the top 'K' numbers, return them in a list
    return list(minheap)


def main():

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
