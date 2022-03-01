# Given the postfix tokens of an arithmetic expression, build and return the binary expression tree that represents this expression.
# Grokking
# Leetcode https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/
# Solution https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/solution/
# Time Complexity Since this algorithm only traverses over the list once, it’s in linear time, O(n).
# Space Complexity The space complexity is O(n).


import abc
from abc import ABC, abstractmethod
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""


class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass


class TreeNode(Node):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def evaluate(self):
        if self.val.isdigit():
            return int(self.val)
        if self.val == "+":
            return self.left.evaluate() + self.right.evaluate()
        elif self.val == "-":
            return self.left.evaluate() - self.right.evaluate()
        elif self.val == "*":
            return self.left.evaluate() * self.right.evaluate()
        elif self.val == "/":
            return self.left.evaluate() // self.right.evaluate()


"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        cur, stack = None, []

        for c in postfix:
            cur = TreeNode(c)
            if not c.isdigit():
                cur.right = stack.pop()
                cur.left = stack.pop()
            stack.append(cur)
        return cur


"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
