# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Grokking
# Leetcode https://leetcode.com/problems/maximum-average-subarray-i/
# Solution https://leetcode.com/problems/maximum-average-subarray-i/solution/
# Sliding Window version
# Time Complexity O(N)
# Space Complexity O(1)


def findMaxAverage(K, arr):
    result = []
    window_sum, window_start = 0.0, 0
    window_avg = -float('inf')
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add the next element

        # slide the window, we don't need to slide if we have hit the required window size K
        if window_end >= K-1:
            window_avg = max(window_avg, window_sum/K)  # append the average
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return window_avg


def main():
    result = findMaxAverage(4, [1, 12, -5, -6, 50, 3])
    print("Maximum Average of subarrays of size K: " + str(result))

    result = findMaxAverage(1, [5])
    print("Maximum Average of subarrays of size K: " + str(result))


main()
