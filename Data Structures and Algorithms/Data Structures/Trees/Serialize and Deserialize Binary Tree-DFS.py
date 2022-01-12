# Serialize a binary tree to a file and then deserialize it back to a tree so that the original and the deserialized trees are identical.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/m7rVmNVXkxE
# Leetcode https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Solution https://leetcode.com/problems/serialize-and-deserialize-binary-tree/solution/
# Time Complexity The runtime complexity of this solution is linear, O(n).
# Space Complexity The memory complexity of this solution is O(h). An iterative solution has O(h) memory complexity as it instantiates a stack
# that has to store information up to the height of the binary tree (h). It will be O(logn) for a balanced tree and, in the worst case, can be O(n).
from BinaryTree import *


class Codec:
    # dfs
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def serialize_rec(node, stream):
            """ a recursive helper function for the serialize() function."""
            if not node:
                stream += "None,"
            else:
                stream += str(node.data)+","
                stream = serialize_rec(node.left, stream)
                stream = serialize_rec(node.right, stream)
            return stream
        return serialize_rec(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def deserialize_rec(list_data):
            """ a recursive helper function for deserialization."""
            if list_data:
                if list_data[0] == "None":
                    list_data.pop(0)
                    return None
                root = BinaryTreeNode(list_data[0])
                list_data.pop(0)
                root.left = deserialize_rec(list_data)
                root.right = deserialize_rec(list_data)
                return root
        d = data.split(",")
        root = deserialize_rec(d)
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
