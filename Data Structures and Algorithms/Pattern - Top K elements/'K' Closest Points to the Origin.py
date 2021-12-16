# Given an array of points in a 2D2D plane, find ‘K’ closest points to the origin.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3YxNVYwNR5p
# Leetcode https://leetcode.com/problems/k-closest-points-to-origin/
# Solution https://leetcode.com/problems/k-closest-points-to-origin/solution/
# Time Complexity The time complexity of this algorithm is O(N*logK) as we iterating all points and pushing them into the heap.
# Space Complexity The space complexity will be O(K) since we need to store the top ‘K’ numbers in the heap.

from __future__ import print_function
from typing import List
from heapq import *


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # used for max-heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    maxheap = []
    # put first 'k' points in the max heap
    for i in range(k):
        heappush(maxheap, points[i])

    # go through the remaining points of the input array, if a point is closer to the origin than the top point
    # of the max-heap, remove the top point from heap and add the point from the input array
    for i in range(k, len(points)):
        if points[i].distance_from_origin() < maxheap[0].distance_from_origin():
            heappop(maxheap)
            heappush(maxheap, points[i])

    # the heap has 'k' points closest to the origin, return them in a list
    return list(maxheap)


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    maxheap = []
    for i in range(k):
        heappush(maxheap, (-L2_norm(points[i]), i))

    for i in range(k, len(points)):
        # check if upper bound of heap is less than current point's L2 norm
        if L2_norm(points[i]) < -maxheap[0][0]:
            heappop(maxheap)
            heappush(maxheap, (-L2_norm(points[i]), i))
    return [points[i] for (_, i) in maxheap]


def L2_norm(point):
    return point[0]**2 + point[1]**2


def main():

    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()

    # direct maxheap solution
    print("\nDirect MaxHeap Solution")
    print(kClosest([[1, 3], [3, 4], [2, -1]], 2))
    print(kClosest([[3, 3], [5, -1], [-2, 4]], 2))
    print(kClosest([[1, 3], [-2, 2]], 1))


main()
