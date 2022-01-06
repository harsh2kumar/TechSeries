# The in-order successor of a node in a binary Search Tree (BST) is the next node in in-order traversal. Write a method to find the in-order
# successor of a given value “d” in a BST.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/g7wVBVxqGJG
# Leetcode https://leetcode.com/problems/inorder-successor-in-bst/
# Solution https://leetcode.com/problems/inorder-successor-in-bst/solution/
# Time Complexity The runtime complexity of this solution is logarithmic, O(logn).
# Space Complexity The space complexity of this solution is constant, O(1).

from BinaryTree import *


def find_min(root):
    # find the min node/ the left most node
    if not root:
        return None
    while root.left:
        root = root.left
    return root


def inorder_successor_bst(root, d):
    if not root:
        return None
    successor = None

    while root:
        # assign parent node as the successor node
        # if d is less than current node's value
        if d < root.data:
            successor = root
            root = root.left
        # if d>curren node's value
        # we cannot assign a successor yet
        # in-order successor will be the minimum value greater than d
        elif d > root.data:
            root = root.right
        # if we have found node with the same value as d
        # check if it has a right node
        # the left most node in its right tree will be the in-order successor
        else:
            if root.right:
                successor = find_min(root.right)
            break

    return successor

# optimized loop condition
# we can simply go to the right node whenever we find node equal to d
# in subsequent iterations it will automatically go to left tree as that condition takes preference


def inorder_successor_leetcode(root, d):
    if not root:
        return None
    successor = None

    while root:
        # assign parent node as the successor node
        # if d is less than current node's value
        if d < root.data:
            successor = root
            root = root.left
        # if d>curren node's value
        # we cannot assign a successor yet
        # in-order successor will be the minimum value greater than d
        ##
        # if we have found node with the same value as d
        # check if it has a right node
        # the left most node in its right tree will be the in-order successor
        elif d >= root.data:
            root = root.right

    return successor


arr = [25, 125, 200, 350, 50, 75, 100]
root = create_BST(arr)
all_data = bst_to_list(root)

for d in all_data:
    successor = inorder_successor_bst(root, d)
    i = all_data.index(d)
    expected_val = None
    if i < len(all_data) - 1:
        expected_val = all_data[i + 1]
    if expected_val != None:
        assert expected_val == successor.data
    else:
        assert successor == None

    if successor:
        print("(" + str(d) + ", " + str(successor.data), end=") ")
    else:
        print("(" + str(d), end=", None)")

print("\nOptimized Loop Condition")
for d in all_data:
    successor = inorder_successor_leetcode(root, d)
    i = all_data.index(d)
    expected_val = None
    if i < len(all_data) - 1:
        expected_val = all_data[i + 1]
    if expected_val != None:
        assert expected_val == successor.data
    else:
        assert successor == None

    if successor:
        print("(" + str(d) + ", " + str(successor.data), end=") ")
    else:
        print("(" + str(d), end=", None)")
