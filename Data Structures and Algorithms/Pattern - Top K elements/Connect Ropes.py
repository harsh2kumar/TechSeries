# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. The cost of connecting two ropes is equal
# to the sum of their lengths.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/qVZmZJVxPY0
# Leetcode https://leetcode.com/problems/minimum-cost-to-connect-sticks/
# Solution https://leetcode.com/problems/minimum-cost-to-connect-sticks/solution/
# Time Complexity Given ‘N’ ropes, we need O(N*logN) to insert all the ropes in the heap. In each step, while processing the heap,
# we take out two elements from the heap and insert one. This means we will have a total of ‘N’ steps, having a total time complexity of O(N*logN).
# Space Complexity The space complexity will be O(N) because we need to store all the ropes in the heap.
from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    minheap = []
    result = 0
    # add all ropes to the min heap
    for i in ropeLengths:
        heappush(minheap, i)
    # go through the values of the heap, in each step take top (lowest) rope lengths from the min heap
    # connect them and push the result back to the min heap.
    # keep doing this until the heap is left with only one rope
    while len(minheap) > 1:
        cost = heappop(minheap)+heappop(minheap)
        heappush(minheap, cost)
        result += cost
    return result


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
