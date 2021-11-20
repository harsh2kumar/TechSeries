# Given a set of investment projects with their respective profits, we need to find the most profitable projects.
# We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose projects that give us the maximum profit.
# Write a function that returns the maximum total capital after selecting the most profitable projects.
# We can start an investment project only when we have the required capital. Once a project is selected, we can assume that its profit has become our capital.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B6x69OLX4jY
# Leetcode https://leetcode.com/problems/ipo/
# Solution https://leetcode.com/problems/ipo/solution/
# Time Complexity TSince, at the most, all the projects will be pushed to both the heaps once, the time complexity of our algorithm is O(NlogN + KlogN),
# where ‘N’ is the total number of projects and ‘K’ is the number of projects we are selecting.
# Space Complexity The space complexity will be O(N) because we will be storing all the projects in the heaps.

from heapq import *


def find_maximum_capital(capital, profits, number_of_projects, initial_capital):
    min_capital_heap = []
    max_profit_heap = []
    # store all project with their capitals in a min heap
    for i in range(len(capital)):
        heappush(min_capital_heap, (capital[i], i))
    available_capital = initial_capital
    # insert all projects with cost less than initial capital
    for i in range(number_of_projects):
        while min_capital_heap and min_capital_heap[0][0] <= available_capital:
            capital, i = heappop(min_capital_heap)
            heappush(max_profit_heap, (-profits[i], i))
        if not max_profit_heap:
            break
        available_capital += -heappop(max_profit_heap)[0]
    return available_capital


def main():

    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
