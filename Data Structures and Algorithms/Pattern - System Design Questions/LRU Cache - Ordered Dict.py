# Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.
# Grokking
# Leetcode https://leetcode.com/problems/max-stack/
# Solution https://leetcode.com/problems/max-stack/solution/
# Time Complexity Since this algorithm only traverses over the list once, it’s in linear time, O(n).
# Space Complexity The space complexity is O(n) because we store all elements in our map.

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
