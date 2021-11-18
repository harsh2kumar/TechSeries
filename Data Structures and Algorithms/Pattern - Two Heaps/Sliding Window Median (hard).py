# Given an array of numbers and a number ‘k’, find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3Y9jm7XRrXO
# Leetcode https://leetcode.com/problems/sliding-window-median/
# Solution https://leetcode.com/problems/sliding-window-median/solution/
# Time Complexity The time complexity of our algorithm is O(N*K) where ‘N’ is the total number of elements in the input array and ‘K’ is the size of the sliding window.
# Space Complexity Ignoring the space needed for the output array, the space complexity will be O(K) because, at any time, we will be storing all
# the numbers within the sliding window.


from heapq import *
import heapq


class SlidingWindowMedian:

    def __init__(self) -> None:
        self.max_heap = []  # containing first half of numbers
        self.min_heap = []  # containing second half of numbers

    def find_sliding_window_median(self, nums, k):
        result = [0. for i in range(len(nums)-k+1)]
        for i in range(len(nums)):
            # insert number in max_heap if its less than or equal to largest number of first half
            # otherwise insert in min_heap
            # heapq doesn't provide default implementation of max_heap, hence negate number when inserting/ deleting
            if not self.max_heap or nums[i] <= -self.max_heap[0]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])

            self.rebalance_heaps()

            if i-k+1 >= 0:  # if we have at least 'k' elements in the sliding window
                # add median of current window to list
                if len(self.min_heap) == len(self.max_heap):
                    # we have even number of elements, take the average of middle two elements
                    result[i-k+1] = -self.max_heap[0]/2.+self.min_heap[0]/2.
                else:  # because max-heap will have one more element than the min-heap
                    result[i-k+1] = -self.max_heap[0]/1.
                # remove the element going out of the sliding window
                element_to_be_removed = nums[i-k+1]
                if element_to_be_removed <= -self.max_heap[0]:
                    self.remove(self.max_heap, -element_to_be_removed)
                else:
                    self.remove(self.min_heap, element_to_be_removed)
                self.rebalance_heaps()
        return result

    def rebalance_heaps(self):
        # balance max_heap and min_heap
        # In case of odd number of total elements, lets decide to have one more element in max_heap than in min_heap
        # either both heaps have equal number of elements or max_heap has one more element than min_heap
        if len(self.max_heap) > len(self.min_heap)+1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
    # removes an element from the heap keeping the heap property

    def remove(self, heap, num):
        index = heap.index(num)  # find the element
        # move the element to the end and delete it
        heap[index] = heap[-1]
        del heap[-1]
        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

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

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
