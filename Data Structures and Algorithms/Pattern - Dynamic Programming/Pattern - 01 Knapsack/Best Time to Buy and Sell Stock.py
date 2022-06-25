# You are given an array prices where prices[i] is the price of a given stock on the ith day. Return the maximum profit you can achieve from this transaction.
# If you cannot achieve any profit, return 0.
# Grokking
# Leetcode https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Solution https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/
# Time Complexity O(n). Only a single pass is needed.
# Space Complexity O(1). Only two variables are used.

from typing import List


class Solution:
    # brute-force
    def maxProfitBrute(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit
    # single-pass

    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i]-min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit


sol = Solution()
print("Brute-Force")
print(sol.maxProfitBrute([7, 1, 5, 3, 6, 4]))
print(sol.maxProfitBrute([7, 6, 4, 3, 1]))
print("Single-Pass")
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
print(sol.maxProfit([7, 6, 4, 3, 1]))
