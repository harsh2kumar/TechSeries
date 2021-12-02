# Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/NE1V3EDAnWN
# Leetcode https://leetcode.com/problems/unique-binary-search-trees/
# Solution https://leetcode.com/problems/unique-binary-search-trees/solution/
# Time Complexity O(N), as one can see, there is one single loop in the algorithm.
# Space Complexity O(1), we use only one variable to store all the intermediate results and the final one.


def count_trees(n):
    """
    :type n: int
    :rtype: int
    """
    C = 1
    for i in range(0, n):
        C = C * 2*(2*i+1)/(i+2)
    return int(C)


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main()
