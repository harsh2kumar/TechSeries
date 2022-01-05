# We are given the root node of a binary tree. We have to write an iterator that takes in this root and iterates through the nodes
# of a binary tree in an in-order way. The expectation is to write two critical methods of any iterator: hasNext() and getNext().
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/m7wOjD0DlBO
# Leetcode https://leetcode.com/problems/binary-search-tree-iterator/
# Solution https://leetcode.com/problems/binary-search-tree-iterator/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The space complexity of this solution is O(h). The recursive solution has O(h) memory complexity as it will consume memory on
# the stack up to the height of binary tree h. It will be O(log n) for a balanced tree and, in the worst case, can be O(n).


from BinaryTree import *


class InorderIterator:
    def __init__(self, root):
        self.stack = []
        self.populate_iterator(root)

    # populate all left nodes
    def populate_iterator(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    # check if stack is empty
    def hasNext(self):
        if self.stack:
            return True
        return False

    # getNext returns null if there are no more elements in tree
    # otherwise pop top of stack and add current node's right child
    # and all of its left children
    def getNext(self):
        if not self.stack:
            return None
        top = self.stack.pop()
        right_child = top.right
        self.populate_iterator(right_child)
        return top


# if you need to provide current element, that will be at top of stack always
def inorder_using_iterator(root):
    iter = InorderIterator(root)
    mystr = ""
    while iter.hasNext():
        ptr = iter.getNext()
        mystr += str(ptr.data) + " "
    return mystr


arr = [25, 125, 200, 300, 75, 50, 12, 35, 60, 75]
root = create_BST(arr)
print("Inorder Iterator = ", end="")
print(inorder_using_iterator(root))
