# There is a dictionary containing words from an alien language for which we don’t know the ordering of the alphabets. Write a method to find the correct order of
# the alphabets in the alien language. It is given that the input is a valid dictionary and there exists an ordering among its alphabets.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/R8AJWOMxw2q
# Leetcode https://leetcode.com/problems/alien-dictionary/
# Solution https://leetcode.com/problems/alien-dictionary/solution/
# Time Complexity The time complexity of the above algorithm will be O(V+E), where ‘V’ is the total number of tasks and ‘E’ is the total number of prerequisites in the graph.
# Space Complexity The space complexity will be O(V+E), since we are storing all of the prerequisites for each vertex in an adjacency list.
from collections import deque


def find_order(words):
    if len(words) <= 0:
        return ""
    sorted_order = []

    # a. Initialize the graph
    in_degree = {}  # count of incoming edges
    graph = {}  # adjacency list graph

    for word in words:
        for char in word:
            in_degree[char] = 0
            graph[char] = []
    # caculate in-degree and build the graph
    for i in range(len(words)-1):
        w1, w2 = words[i], words[i+1]
        for j in range(min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                in_degree[child] += 1
                graph[parent].append(child)
                break  # only the first different character between the two words will help us find the order
        else:  # Check that second word isn't a prefix of first word.
            if len(w2) < len(w1):
                return ""

    # find out sources
    # c. Find all sources i.e., all tasks with 0 in-degrees
    sources = deque()
    for char, in_d in in_degree.items():
        if in_d == 0:
            sources.append(char)

    # build topological order
    # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
    # if a child's in-degree becomes zero, add it to the sources queue
    # if sortedOrder doesn't contain all tasks, there is a cyclic dependency between tasks, therefore, we
    # will not be able to schedule all tasks
    while sources:
        char = sources.popleft()
        sorted_order.append(char)
        for child in graph[char]:
            # get the node's children to decrement their in-degrees
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    # topological sort is not possible as the graph has a cycle
    # if sortedOrder doesn't contain all characters, there is a cyclic dependency between characters, therefore, we
    # will not be able to find the correct ordering of the characters
    if len(sorted_order) != len(in_degree):
        return ""
    return "".join(sorted_order)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " +
          find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))
    print("Character order: " + find_order(["abc", "ab"]))


main()
