# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled.
# Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/q2YmVjQMMr3
# Leetcode
# Solution
# Time Complexity & Space Complexity
# If we don’t have any prerequisites, all combinations of the tasks can represent a topological ordering. As we know, that there can be N!N! combinations for ‘N’ numbers,
# therefore the time and space complexity of our algorithm will be O(V! * E) where ‘V’ is the total number of tasks and ‘E’ is the total prerequisites.
# We need the ‘E’ part because in each recursive call, at max, we remove (and add back) all the edges.
from collections import deque


def print_orders(tasks, prerequisites):
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

    print_all_task_orders(graph, in_degree, sources, sorted_order)


def print_all_task_orders(graph, in_degree, sources, sorted_order):
    if sources:
        for vertex in sources:
            sorted_order.append(vertex)
            sources_for_next_call = deque(sources)  # make a copy of sources
            # only remove the current source, all other sources should remain in the queue for the next call
            sources_for_next_call.remove(vertex)
            for child in graph[vertex]:
                # get the node's children to decrement their in-degrees
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources_for_next_call.append(child)

            # recursive call to print other orderings from the remaining (and new) sources
            print_all_task_orders(
                graph, in_degree, sources_for_next_call, sorted_order)

            # backtrack, remove the vertex from the sorted order and put all of its children back to consider
            # the next source instead of the current vertex
            sorted_order.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] += 1

    # if sortedOrder doesn't contain all tasks, either we've a cyclic dependency between tasks, or
    # we have not processed all the tasks in this recursive call
    if len(sorted_order) == len(in_degree):
        print(sorted_order)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()
