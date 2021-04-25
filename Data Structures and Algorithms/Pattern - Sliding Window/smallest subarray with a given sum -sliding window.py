# Given an array, find the max subarray sum of all contiguous subarrays of size ‘K’ in it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ
# Time Complexity O(N)
# Space Complexity O(1)

import math


def smallest_subarray_with_given_sum(s, arr):
    window_sum, min_window_len = 0.0, math.inf
    window_start = 0
    for window_end in range(len(arr)):
        # expand the window
        window_sum += arr[window_end]
        while window_sum >= s:
            # shrink the window while the sum is greater than or equal to target sum
            min_window_len = min(min_window_len, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_window_len == math.inf:
        return 0
    return min_window_len

def main():
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " +
          str(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6])))


main()
