# Design a class to calculate the median of a number stream.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3Yj2BmpyEy4
# Leetcode https://leetcode.com/problems/find-median-from-data-stream/
# Solution https://leetcode.com/problems/find-median-from-data-stream/solution/
# Time Complexity The time complexity of the insertNum() will be O(logN) due to the insertion in the heap.
# The time complexity of the findMedian() will be O(1)O as we can find the median from the top elements of the heaps.
# Space Complexity The space complexity will be O(N) because, as at any time, we will be storing all the numbers.

from heapq import *


class MedianOfAStream:

    def __init__(self) -> None:
        self.max_heap = []  # containing first half of numbers
        self.min_heap = []  # containing second half of numbers

    def insert_num(self, num):
        # insert number in max_heap if its less than or equal to largest number of first half
        # otherwise insert in min_heap
        # heapq doesn't provide default implementation of max_heap, hence negate number when inserting/ deleting
        if not self.max_heap or num <= -self.max_heap[0]:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        # balance max_heap and min_heap
        # In case of odd number of total elements, lets decide to have one more element in max_heap than in min_heap
        # either both heaps have equal number of elements or max_heap has one more element than min_heap
        if len(self.max_heap) > len(self.min_heap)+1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self) -> float:
        # even number of elements
        # if both heaps contain equal number of elements, return average of middle two elements
        if len(self.max_heap) == len(self.min_heap):
            return -self.max_heap[0]/2. + self.min_heap[0]/2.
        # odd number of elements
        # return top element from max_heap
        else:
            return -self.max_heap[0]/1.


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
