# Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/NE1V3EDAnWN
# Leetcode https://leetcode.com/problems/unique-binary-search-trees/
# Solution https://leetcode.com/problems/unique-binary-search-trees/solution/
# Time Complexity The overall time complexity of the algorithm will be O(N*2^N). Check Notion for accurately calculating overall complexity.
# Space Complexity All the additional space used by our algorithm is for the output list. Since we can have a total of O(2^N) combinations, the space complexity
# of our algorithm is O(N*2^N).

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_trees(n):
    return count_trees_rec({}, n)


def count_trees_rec(map, n):
    if n in map:
        return map[n]
    # if n<=1, return 1, as only one tree can be formed
    if n <= 1:
        return 1
    count = 0
    # need n+1, as n should also be included as a node in our tree
    for i in range(1, n+1):
        # count number of left and right subtrees if i is root
        left_subtree = count_trees(i-1)
        right_subtree = count_trees(n-i)
        # take cartesian product to find the count of trees in total
        count += left_subtree*right_subtree
    map[n] = count

    return count


def main():
    print("Total trees: " + str(count_trees(2)))
    print("Total trees: " + str(count_trees(3)))


main()
