# Given a directed graph, find the topological ordering of its vertices.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/m25rBmwLV00
# Leetcode
# Solution
# Time Complexity The time complexity of the above algorithm will be O(V+E), where ‘V’ is the total number of vertices and ‘E’ is the total number of edges in the graph.
# Space Complexity The space complexity will be O(V+E), since we are storing all of the edges for each vertex in an adjacency list.
from collections import deque


def topological_sort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return sorted_order

    # a. Initialize the graph
    in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjacency list graph

    # caculate in-degree and build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        in_degree[child] += 1  # increment child's inDegree
        graph[parent].append(child)  # put the child into it's parent's list

    # find out sources
    # c. Find all sources i.e., all vertices with 0 in-degrees
    sources = deque()
    for vertex, in_d in in_degree.items():
        if in_d == 0:
            sources.append(vertex)

    # build topological order
    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
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
    if len(sorted_order) != vertices:
        return False
    return True


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
