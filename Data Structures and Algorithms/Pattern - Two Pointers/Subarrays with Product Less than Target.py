# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RMV1GV1yPYz
# Time Complexity The main for-loop managing the sliding window takes O(N) but creating subarrays can take up to O(N^2) in the worst case.
# Therefore overall, our algorithm will take O(N^3).
# Space Complexity At worst, each subarray can take O(n) space, so overall, our algorithm’s space complexity will be O(n^3).

from  collections import deque

def find_subarrays(arr, target):
    result = []
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while left<len(arr) and product>=target:
            product /= arr[left]
            left += 1
        temp_deque = deque()
        for i in range(right, left-1, -1):
            temp_deque.appendleft(arr[i])
            result.append(list(temp_deque))
    return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))
  print(find_subarrays([1, 2, 3], 0))


main()