# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards. Your score is the sum of the points
# of the cards you have taken. Given the integer array cardPoints and the integer k, return the maximum score you can obtain.
# Grokking
# Leetcode https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
# Solution https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/solution/
# Sliding Window version
# Time Complexity O(N)
# Space Complexity O(1)


from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        window_sum, window_size = 0, len(cardPoints)-k
        if window_size == 0:
            return sum(cardPoints)
        window_start, window_end = 0, 0
        total_sum = sum(cardPoints)
        max_score, min_sum = -float('inf'), float('inf')

        # expansion phase
        for window_end in range(len(cardPoints)):
            window_sum += cardPoints[window_end]

            # shrinking phase
            if window_end-window_start+1 == window_size:
                if min_sum > window_sum:
                    min_sum = min(min_sum, window_sum)
                    max_score = total_sum-min_sum
                window_sum -= cardPoints[window_start]
                window_start += 1
        return max_score


sol = Solution()
print("[1,2,3,4,5,6,1], 3: ", sol.maxScore([1, 2, 3, 4, 5, 6, 1], 3))
print("[2,2,2], 2: ", sol.maxScore([2, 2, 2], 2))
print("[9,7,7,9,7,7,9], 7: ", sol.maxScore([9, 7, 7, 9, 7, 7, 9], 7))
