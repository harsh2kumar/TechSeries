# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
# Grokking 
# Leetcode https://leetcode.com/problems/symmetric-tree/
# Solution https://leetcode.com/problems/symmetric-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The space complexity of this solution is O(h). The recursive solution has O(h) memory complexity as it will consume memory on
# the stack up to the height of binary tree h. It will be O(log n) for a balanced tree and, in the worst case, can be O(n).


from BinaryTree import *


def is_symmetric(root) -> bool:
    return is_mirror(root, root)


def is_mirror(root1, root2) -> bool:
     # check if both nodes are empty
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    # if both nodes are non-empty check their data
    # and validate their child nodes
    return (root1.data == root2.data) and is_mirror(root1.left, root2.right) and is_mirror(root1.right, root2.left)


arr1 = [100, 50, 200, 25, 125, 350]
root1 = create_BST(arr1)
display_level_order(root1)
if(is_symmetric(root1)):
    print("The tree is symmetric")
else:
    print("The tree is not symmetric")

arr2 = [1, 2, 10, 50, 180, 199]
root2 = create_BST(arr2)
display_level_order(root2)
if(is_symmetric(root2)):
    print("The tree is symmetric")
else:
    print("The tree is not symmetric")

arr3 = [1, 2, 2, 3, 4, 4, 3]
root3 = create_BST(arr3)
display_level_order(root3)
if(is_symmetric(root3)):
    print("The tree is symmetric")
else:
    print("The tree is not symmetric")
