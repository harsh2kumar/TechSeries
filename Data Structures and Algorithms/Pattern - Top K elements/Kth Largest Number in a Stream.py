# Check Problem Statement
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B819G5DZBxX
# Leetcode https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Solution https://leetcode.com/problems/kth-largest-element-in-a-stream/solution/
# Time Complexity The time complexity of the add() function will be O(logK) since we are inserting the new number in the heap.
# Space Complexity The space complexity will be O(K) for storing numbers in the heap.
from heapq import *


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.minheap = []
        self.k = k
        # add the numbers in the min heap
        for num in nums:
            self.add(num)

    def add(self, num):
        # add the new number in the min heap
        heappush(self.minheap, num)

        # if heap has more than 'k' numbers, remove one number
        if len(self.minheap) > self.k:
            heappop(self.minheap)

        # return the 'Kth largest number
        return self.minheap[0]


def main():

    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
