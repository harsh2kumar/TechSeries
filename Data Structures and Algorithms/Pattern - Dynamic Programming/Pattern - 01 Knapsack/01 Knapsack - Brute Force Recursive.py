# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which will give us maximum profit such that
# their cumulative weight is not more than a given number ‘C.’ Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/gkZNLjV2kBk#Problem-Statement
# Leetcode
# Solution
# Time Complexity he above algorithm’s time complexity is exponential O(2^n), where ‘n’ represents the total number of items.
# This can also be confirmed from the above recursion tree. As we can see, we will have a total of ‘31’ recursive calls – calculated through (2^n) + (2^n) - 1,
# which is asymptotically equivalent to O(2^n).
# Space Complexity The space complexity is O(n). This space will be used to store the recursion stack. Since the recursive algorithm works in a depth-first fashion,
# which means that we can’t have more than ‘n’ recursive calls on the call stack at any time.


def solve_knapsack(profits, weights, capacity):
    return recursive_knapsack(profits, weights, capacity, 0)


def recursive_knapsack(profits, weights, capacity, current_index):
    # base case
    if capacity <= 0 or current_index >= len(profits):
        return 0
    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we  shouldn't process this
    profit_s = 0
    if weights[current_index] <= capacity:
        profit_s = profits[current_index] + recursive_knapsack(
            profits, weights, capacity-weights[current_index], current_index+1)
    # recursive call after excluding the element at the currentIndex
    profit_i = recursive_knapsack(profits, weights, capacity, current_index+1)

    return max(profit_s, profit_i)


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
