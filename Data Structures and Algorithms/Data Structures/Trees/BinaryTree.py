from collections import deque
from random import random


class TreeNode:
    def __init__(self, data):
        if data is None:
            data = 0
        self.data = data
        self.val = data
        self.left = None
        self.right = None


class BinaryTreeNode:
    def __init__(self, data):
        if data is None:
            data = 0
        self.data = data
        self.val = data
        self.left = None
        self.right = None

        # below data members used only for some of the problems
        self.next = None
        self.parent = None
        self.count = None


def insert(root, d):
    if d is None:
        d = 0
    pNew = BinaryTreeNode(d)
    if root == None:
        return pNew

    parent = None
    pTemp = root
    while (pTemp != None):
        parent = pTemp
        if d < pTemp.data:
            pTemp = pTemp.left
        else:
            pTemp = pTemp.right

    if d < parent.data:
        parent.left = pNew
    else:
        parent.right = pNew

    return root


def find_in_bst(root, d):
    if root == None:
        return None

    if root.data == d:
        return root
    elif root.data > d:
        return find_in_bst(root.left, d)
    else:
        return find_in_bst(root.right, d)

# find node in inorder
# works for both BST and binary tree


def find_node(root, d):
    if root == None:
        return

    if root.data == d:
        return root

    temp = find_node(root.left, d)
    if temp != None:
        return temp

    return find_node(root.right, d)


def display_inorder(node):
    if node == None:
        return

    display_inorder(node.left)
    print(str(node.data), end=", ")
    display_inorder(node.right)


def create_BST(arr):
    root = None
    for x in arr:
        root = insert(root, x)
    return root


def create_binary_tree(count):
    root = None
    for i in range(1, count):
        root = insert(root, random.randrange(1, 100))
    return root


def create_random_BST(count):
    root = None
    for i in range(1, count):
        root = insert(root, random.randrange(200, 300))
    return root


def bst_to_list_rec(root, lst):
    if root == None:
        return

    bst_to_list_rec(root.left, lst)
    lst.append(root.data)
    bst_to_list_rec(root.right, lst)


def bst_to_list(root):
    lst = []
    bst_to_list_rec(root, lst)
    return lst


def insert_at_head(head, data):
    newNode = LinkedListNode(data)
    newNode.next = head
    return newNode


def populate_parents_rec(root, parent):
    if root == None:
        return
    root.parent = parent

    populate_parents_rec(root.left, root)
    populate_parents_rec(root.right, root)


def populate_parents(root):
    populate_parents_rec(root, None)


def display_level_order(root):
    if root == None:
        return
    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()
        print(str(temp.data), end=",")
        if temp.left != None:
            q.append(temp.left)
        if temp.right != None:
            q.append(temp.right)

    print()


def get_level_order(root):
    output = []
    if root == None:
        return output

    q = deque()
    q.append(root)

    while q:
        temp = q.popleft()
        output.append(temp.data)
        if temp.left != None:
            q.append(temp.left)
        if temp.right != None:
            q.append(temp.right)

    return output


def get_inorder_helper(root, output):
    if root == None:
        return output

    output = get_inorder_helper(root.left, output)
    output.append(root.data)
    output = get_inorder_helper(root.right, output)

    return output


def get_inorder(root):
    output = []
    return get_inorder_helper(root, output)


def is_identical_tree(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 != None and root2 != None and root1.data == root2.data:
        return is_identical_tree(root1.left, root2.left) and is_identical_tree(root1.right, root2.right)

    return False
