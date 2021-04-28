# Given a binary array, find the longest contiguous subarray containing only ones given that you are allowed to replace 'k' zeroes with ones
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B6VypRxPolJ
# Leetcode https://leetcode.com/problems/max-consecutive-ones-iii/
# Solution https://leetcode.com/problems/max-consecutive-ones-iii/solution/
# Time Complexity O(N)
# Space Complexity O(1)


def length_of_longest_substring(arr, k):
    window_start, max_length = 0, 0
    max_ones_count = 0
    
    # Try to extend the range [window_start, window_end]
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1
        # Current window size is from window_start to window_end, overall we have a maximum of 1s
        # repeating 'max_ones_count' times, this means we can have a window with 'max_ones_count' 1s
        # and the remaining are 0s which should replace with 1s.
        # now, if the remaining 0s are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' 0s
        if (window_end-window_start+1-max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1
        # remember max length
        max_length = max(max_length, window_end-window_start+1)
    return max_length


def main():
    print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(length_of_longest_substring(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
