# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Grokking
# Leetcode https://leetcode.com/problems/lru-cache/
# Solution https://leetcode.com/problems/lru-cache/solution/
# Time Complexity O(1) both for put and get since all operations with ordered dictionary : get/in/set/move_to_end/popitem (get/containsKey/put/remove) are
# done in a constant time.
# Space Complexity O(capacity) since the space is used only for an ordered dictionary with at most capacity + 1 elements.

from collections import OrderedDict


class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


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
