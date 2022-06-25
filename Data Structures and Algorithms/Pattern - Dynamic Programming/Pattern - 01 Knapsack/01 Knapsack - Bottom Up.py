# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that
# their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/gkZNLjV2kBk#Problem-Statement
# Leetcode
# Solution
# Time CSince our memoization array dp[profits.length][capacity+1] stores the results for all subproblems, we can conclude that we will not have more than N*C subproblems
# (where ‘N’ is the number of items and ‘C’ is the knapsack capacity). This means that our time complexity will be O(N*C).
# Space Complexity The above algorithm will use O(N*C) space for the memoization array. Other than that, we will use O(N) space for the recursion call-stack.
# So the total space complexity will be O(N*C + N), which is asymptotically equivalent to O(N*C).

def solve_knapsack(profits, weights, capacity):
    # basic checks
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[0 for x in range(capacity+1)] for y in range(n)]

    # populate the capacity = 0 columns, with '0' capacity and '0' profit
    for i in range(n):
        dp[i][0] = 0

    # if we have only one weight, we will take it if it is not more than the capacity
    for c in range(capacity+1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    # process all sub-arrays for all capacities
    for i in range(1, n):
        for c in range(capacity+1):
            profit_include, profit_exclude = 0, 0
            # include the item, if it is not more than the capacity
            if weights[i] <= c:
                profit_include = profits[i] + dp[i-1][c-weights[i]]
            # exclude the items
            profit_exclude = dp[i-1][c]
            # take maximum of the two
            dp[i][c] = max(profit_include, profit_exclude)
    # maximum profit will be at the bottom right corner
    return dp[n-1][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
