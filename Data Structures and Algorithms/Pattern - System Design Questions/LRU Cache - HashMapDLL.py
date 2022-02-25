# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Grokking
# Leetcode https://leetcode.com/problems/lru-cache/
# Solution https://leetcode.com/problems/lru-cache/solution/
# Time Complexity O(1) both for put and get.
# Space Complexity O(capacity) since the space is used only for a hashmap and double linked list with at most capacity + 1 elements.

class DLinkedNode():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.size = 0

        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """
        Always add new node right after head
        """
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        remove exisiting node form DLL
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        move certain node in between to the head
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        pop the current tail
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key):
        node = self.cache.get(key, None)

        if not node:
            return -1

        # move the accessed node to head
        self._move_to_head(node)
        return node.value

    def put(self, key, value):
        node = self.cache.get(key, None)

        if not node:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self._add_node(node)
            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = key
            self._move_to_head(node)


sol = LRUCache(2)
print(sol.put(1, 1))
print(sol.put(2, 2))
print(sol.get(1))
print(sol.put(3, 3))
print(sol.get(2))
print(sol.put(4, 4))
print(sol.get(1))
print(sol.get(3))
print(sol.get(4))
