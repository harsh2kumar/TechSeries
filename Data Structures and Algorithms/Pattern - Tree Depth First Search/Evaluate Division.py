# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
# Each Ai or Bi is a string that represents a single variable. Return the answers to all queries. If a single answer cannot be determined, return -1.0.
# Grokking
# Leetcode https://leetcode.com/problems/evaluate-division/
# Solution https://leetcode.com/problems/evaluate-division/solution/
# Let N be the number of input equations and M be the number of queries.
# Time Complexity The time complexity of the above algorithm is O(M⋅N)
# Space Complexity Tour algorithm’s overall space complexity is O(N).

from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)

        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product*value, visited)
                    if ret != -1:
                        break
            visited.remove(curr_node)
            return ret

        # building the graph
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # evaluate each query via Backtracking(DFS)
        # by verifying whether a path exists from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # either node doesn't exist
                ret = -1
            elif dividend == divisor:
                # origin and destination are same
                ret = 1
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)

        return results


sol = Solution()
print(sol.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0], [
      ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
print(sol.calcEquation([["a", "b"], ["b", "c"], ["bc", "cd"]], [
      1.5, 2.5, 5.0], [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]))
print(sol.calcEquation([["a", "b"]], [0.5], [
      ["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]))
