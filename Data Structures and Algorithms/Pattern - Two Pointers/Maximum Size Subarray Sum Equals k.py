# Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.
# Grokking
# Leetcode https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
# Solution https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/solution/
# Sliding Window version
# Time Complexity O(N)
# Space Complexity O(N)


def maxSubArrayLen(K, arr):
    # we construct prefix Sum HashTable
    window_sum, window_start = 0, 0
    prefix_sum_indices = {}
    max_size = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        # Check if all of the numbers seen so far sum to k.
        if window_sum == K:
            max_size = window_end-window_start+1
        # If any subarray seen so far sums to k, then
        # update the length of the longest_subarray.
        if window_sum-K in prefix_sum_indices:
            max_size = max(max_size, window_end - prefix_sum_indices[window_sum-K])
        # Only add the current prefix_sum index pair to the
        # map if the prefix_sum is not already in the map.
        if window_sum not in prefix_sum_indices:
            prefix_sum_indices[window_sum] = window_end
    return max_size


def main():
    result = maxSubArrayLen(3, [1, -1, 5, -2, 3])
    print("Longest subarray with sum K: " + str(result))

    result = maxSubArrayLen(1, [-2, -1, 2, 1])
    print("Longest subarray with sum K: " + str(result))


main()
