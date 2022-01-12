# Given the root node of a binary tree, print the nodes that form the boundary (perimeter).
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/m7rVmNVXkxE
# Leetcode https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Solution https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The memory complexity of this solution is O(h). An iterative solution has O(h) memory complexity as it instantiates a stack
# that has to store information up to the height of the binary tree (h). It will be O(logn) for a balanced tree and, in the worst case, can be O(n).
from BinaryTree import *
from collections import deque


class Codec:
    # bfs
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # perform level order traversal
        if not root:
            return ""
        queue = deque()
        queue.append(root)
        result = ""
        while queue:
            node = queue.popleft()
            if not node:
                result += "None,"
                continue
            result += str(node.data)+","
            queue.append(node.left)
            queue.append(node.right)
        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data_list = data.split(",")
        root = BinaryTreeNode(int(data_list[0]))
        queue = deque()
        queue.append(root)
        i = 1  # start with next node
        while queue and i < len(data_list):
            node = queue.popleft()
            # level order traversal
            if data_list[i] != "None":
                left = BinaryTreeNode(int(data_list[i]))
                node.left = left
                queue.append(left)
            i += 1
            if data_list[i] != "None":
                right = BinaryTreeNode(int(data_list[i]))
                node.right = right
                queue.append(right)
            i += 1
        return root


arr = [100, 50, 200, 25, 75, 125, 350]
root = create_BST(arr)
print("Original: ", end="")
display_level_order(root)
ser = Codec()
deser = Codec()
print("Serialized: ", ser.serialize(root))
ans = deser.deserialize(ser.serialize(root))
print("Deserialized: ", end="")
display_level_order(ans)
