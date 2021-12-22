# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
# Given the number of tasks and a list of prerequisite pairs, write a method to find the ordering of tasks we should pick to finish all tasks.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/BnnArPGKolJ
# Leetcode https://leetcode.com/problems/course-schedule-ii/
# Solution https://leetcode.com/problems/course-schedule-ii/solution/
# Time Complexity The time complexity of the above algorithm will be O(V+E), where ‘V’ is the total number of tasks and ‘E’ is the total number of prerequisites in the graph.
# Space Complexity The space complexity will be O(V+E), since we are storing all of the prerequisites for each vertex in an adjacency list.
from collections import deque


def is_scheduling_possible(tasks, prerequisites):
    sorted_order = []

    # a. Initialize the graph
    in_degree = {i: 0 for i in range(tasks)}  # count of incoming edges
    graph = {i: [] for i in range(tasks)}  # adjacency list graph

    # caculate in-degree and build the graph
    for edge in prerequisites:
        parent, child = edge[0], edge[1]
        in_degree[child] += 1  # increment child's inDegree
        graph[parent].append(child)  # put the child into it's parent's list

    # find out sources
    # c. Find all sources i.e., all tasks with 0 in-degrees
    sources = deque()
    for vertex, in_d in in_degree.items():
        if in_d == 0:
            sources.append(vertex)

    # build topological order
    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    # if sortedOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
    # will not be able to schedule all tasks
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            # get the node's children to decrement their in-degrees
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    # check if there are no cycles
    if len(sorted_order) != tasks:
        return []
    return sorted_order


def main():
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))
    print("Is scheduling possible: " +
          str(is_scheduling_possible(1, [])))


main()
