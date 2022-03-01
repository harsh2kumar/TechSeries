# Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.
# Grokking
# Leetcode https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
# Solution https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/solution/
# Time Complexity O(N)
# Space Complexity O(1)


from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        # find the window size
        # it is equal to number of ones
        k = 0
        for num in data:
            if num == 1:
                k += 1
        # sliding window to calculate the min num of swaps needed
        window_start, window_end = 0, 0
        total_ones, ones_current_window = k, 0
        min_swaps = float('inf')
        # expansion phase
        for window_end in range(len(data)):
            if data[window_end] == 1:
                ones_current_window += 1
            # shrinking phase
            if window_end-window_start+1 >= k:
                # min swaps will be the count of zeros in the current window
                # or total ones - ones in current window
                min_swaps = min(min_swaps, total_ones-ones_current_window)
                # remove outgoing ones
                if data[window_start] == 1:
                    ones_current_window -= 1
                window_start += 1
        return min_swaps


sol = Solution()
print("[1,0,1,0,1]: ", sol.minSwaps([1, 0, 1, 0, 1]))
print("[0,0,0,1,0]: ", sol.minSwaps([0, 0, 0, 1, 0]))
print("[1,0,1,0,1,0,0,1,1,0,1]: ", sol.minSwaps(
    [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]))
print("[1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]: ",
      sol.minSwaps([1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]))
