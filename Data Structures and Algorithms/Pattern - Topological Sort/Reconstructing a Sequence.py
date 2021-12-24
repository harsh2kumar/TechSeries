# Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.
# Or check if its the shortest sequence that can be constructed.(Same as Unique sequence)
# Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in the array are subsequences of it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/m7VAO5OrQr3
# Leetcode https://leetcode.com/problems/sequence-reconstruction/
# Solution https://leetcode.com/problems/sequence-reconstruction/solution/
# Time Complexity The time complexity of the above algorithm will be O(V+E), where ‘V’ is the total number of tasks and ‘E’ is the total number of prerequisites in the graph.
# Space Complexity The space complexity will be O(V+E), since we are storing all of the prerequisites for each vertex in an adjacency list.
from collections import deque


def can_construct(originalSeq, sequences):
    if len(originalSeq) <= 0:
        return False
    sorted_order = []

    # a. Initialize the graph
    in_degree = {}  # count of incoming edges
    graph = {}  # adjacency list graph

    for seq in sequences:
        for num in seq:
            in_degree[num] = 0
            graph[num] = []
    # caculate in-degree and build the graph
    for seq in sequences:
        for i in range(1, len(seq)):
            parent, child = seq[i-1], seq[i]
            in_degree[child] += 1
            graph[parent].append(child)

    if len(in_degree) != len(originalSeq):
        return False
    # find out sources
    # c. Find all sources i.e., all tasks with 0 in-degrees
    sources = deque()
    for num, in_d in in_degree.items():
        if in_d == 0:
            sources.append(num)

    # build topological order
    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    # if sortedOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
    # will not be able to schedule all tasks
    while sources:
        # more than one sources mean, there is more than one way to reconstruct the sequence
        # the next source(or number) is different from the original sequence
        if len(sources) > 1 or originalSeq[len(sorted_order)] != sources[0]:
            return False
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            # get the node's children to decrement their in-degrees
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    # if sortedOrder doesn't contain all characters, there is a cyclic dependency between characters, therefore, we
    # will not be able to find the correct ordering of the characters
    # if sortedOrder's size is not equal to original sequence's size, there is no unique way to construct
    return len(sorted_order) == len(originalSeq)


def main():
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
          str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
          str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))
    print("Can construct: " +
          str(can_construct([1, 2, 3], [[1, 2], [1, 3], [2, 3]])))


main()
