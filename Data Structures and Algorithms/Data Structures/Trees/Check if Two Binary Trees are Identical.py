# Given the roots of two binary trees, determine if these trees are identical or not. Identical trees have the same layout and data at each node.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/3Yjr45ygKV4
# Leetcode https://leetcode.com/problems/same-tree/
# Solution https://leetcode.com/problems/same-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The space complexity of this solution is O(h). The recursive solution has O(h) memory complexity as it will consume memory on
# the stack up to the height of binary tree h. It will be O(log n) for a balanced tree and, in the worst case, can be O(n).


from BinaryTree import *


def are_identical(root1, root2):
    # check if both nodes are empty
    if root1 == None and root2 == None:
        return True
    # if both nodes are non-empty check their data
    # and validate their child nodes
    if root1 != None and root2 != None:
        return (root1.data == root2.data and
                are_identical(root1.left, root2.left) and
                are_identical(root1.right, root2.right))
    # if both nodes are not same
    # return False
    return False


arr1 = [100, 50, 200, 25, 125, 350]
arr2 = [1, 2, 10, 50, 180, 199]
root1 = create_BST(arr1)
display_level_order(root1)
root2 = create_BST(arr2)

display_level_order(root2)
if(are_identical(root1, root2)):
    print("The trees are identical")
else:
    print("The trees are not identical")
