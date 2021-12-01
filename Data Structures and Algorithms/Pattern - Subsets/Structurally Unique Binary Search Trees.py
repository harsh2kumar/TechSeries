# Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/xVQyDZBMpKE
# Leetcode https://leetcode.com/problems/unique-binary-search-trees-ii/
# Solution https://leetcode.com/problems/unique-binary-search-trees-ii/solution/
# Time Complexity The overall time complexity of the algorithm will be O(N*2^N). Check Notion for accurately calculating overall complexity.
# Space Complexity All the additional space used by our algorithm is for the output list. Since we can have a total of O(2^N) combinations, the space complexity
# of our algorithm is O(N*2^N).

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_unique_trees(n):
    # if n<=0, return empty list
    if n <= 0:
        return []
    return find_unique_trees_rec(1, n)


def find_unique_trees_rec(start, end):
    result = []
    if start > end:
        result.append(None)
    # need to include both start and end values in our binary tree
    for i in range(start, end+1):
        left_tree = find_unique_trees_rec(start, i-1)
        right_tree = find_unique_trees_rec(i+1, end)

        root = TreeNode(i)
        root.left = left_tree
        root.right = right_tree
        result.append(root)
    return result


def main():
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


main()
