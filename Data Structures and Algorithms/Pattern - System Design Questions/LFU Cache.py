# Design a data structure that follows the constraints of a Least Frequently Used (LFU) cache.
# Grokking
# Leetcode https://leetcode.com/problems/lfu-cache/
# Solution https://leetcode.com/problems/lfu-cache/solution/
# Time Complexity O(1) both for put and get.
# Space Complexity O(capacity) since the space is used only for a hashmap and double linked list with at most capacity + 1 elements.

from collections import defaultdict, OrderedDict


class Node:
    def __init__(self, value, count):
        self.value = value
        self.count = count


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodeKeys = {}
        self.nodeCount = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key: int) -> int:
        # if key is not present in LFU cache
        if key not in self.nodeKeys:
            return -1
        # if we have it, then we need to increase its count by 1
        node = self.nodeKeys[key]
        del self.nodeCount[node.count][key]

        # space optimization
        if not self.nodeCount[node.count]:
            del self.nodeCount[node.count]

        # increment node count
        node.count += 1
        self.nodeCount[node.count][key] = node

        # update minimum count
        if not self.nodeCount[self.minCount]:
            self.minCount += 1

        return node.value

    def put(self, key: int, value: int) -> None:
        # if the capacity is None, we cannot store anything in our LFU cache
        if not self.capacity:
            return

        if key in self.nodeKeys:
            self.nodeKeys[key].value = value
            self.get(key)
            return

        # remove LFU key if capacity is reached
        if len(self.nodeKeys) == self.capacity:
            # pop the least recently used item with the least frequency
            lfuKey, _ = self.nodeCount[self.minCount].popitem(last=False)
            del self.nodeKeys[lfuKey]

        # add new node and set its count to 1
        newNode = Node(value, 1)
        self.nodeKeys[key] = newNode
        self.nodeCount[1][key] = newNode
        self.minCount = 1  # set min count


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
