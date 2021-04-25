# Given an array, find the max subarray sum of all contiguous subarrays of size ‘K’ in it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/JPKr0kqLGNP
# Time Complexity O(N)
# Space Complexity O(1)


def max_sub_array_of_size_k(k, arr):
    maxSum, maxSubArrayIndice = -1, []
    windowSum, windowStart = 0.0, 0

    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd]
        if windowEnd >= k-1:
            if windowSum > maxSum:
                maxSum = windowSum
                maxSubArrayIndice = [windowStart, windowEnd]
            windowSum -= arr[windowStart]
            windowStart += 1
    return maxSum


def main():
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))


main()
