# Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/NE1V3EDAnWN
# Leetcode https://leetcode.com/problems/unique-binary-search-trees/
# Solution https://leetcode.com/problems/unique-binary-search-trees/solution/
# Time Complexity The overall time complexity of the algorithm will be O(N^2). Check Notion for accurately calculating overall complexity.
# Space Complexity The space complexity of the above algorithm is mainly the storage to keep all the intermediate solutions, therefore O(N).


def count_trees(n):
    """
    :type n: int
    :rtype: int
    """
    G = [0]*(n+1)
    G[0], G[1] = 1, 1

    for i in range(2, n+1):
        for j in range(1, i+1):
            G[i] += G[j-1] * G[i-j]

    return G[n]


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main()
