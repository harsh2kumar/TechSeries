# Given an unsorted array of numbers, find Kth smallest number in it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/gxxPGn8vE8G
# Leetcode
# Solution
# Time Complexity As discussed above, the time complexity of this algorithm is O(K*logK+(N-K)*logK), which is asymptotically equal to O(N*logK)
# Space Complexity The space complexity will be O(K) since we need to store the top ‘K’ numbers in the heap.
from heapq import *


def find_Kth_smallest_number(nums, k):
    maxheap = []
    # put first 'K' numbers in the min heap
    for i in range(k):
        heappush(maxheap, -nums[i])
    # go through the remaining numbers of the array, if the number from the array is smaller than the
    # top(biggest) number of the heap, remove the top number from heap and add the number from array
    for i in range(k, len(nums)):
        if -nums[i] > maxheap[0]:
            heappop(maxheap)
            heappush(maxheap, -nums[i])
    # the root of the heap has the Kth smallest number
    return -maxheap[0]


def main():

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()
