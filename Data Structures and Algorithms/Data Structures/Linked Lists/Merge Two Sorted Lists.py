# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# Grokking
# Leetcode https://leetcode.com/problems/merge-two-sorted-lists/
# Solution https://leetcode.com/problems/merge-two-sorted-lists/solution/
# Time Complexity: The time complexity of our algorithm will be O(N+M) where ‘N’ & M are the total number of nodes in two LinkedLists.
# Space Complexity: [Iterative solution] We only used constant space, therefore, the space complexity of our algorithm is O(1).
# Space Complexity: [Recursive solution] O(N+M). The first call to mergeTwoLists does not return until the ends of both l1 and l2 have been reached, so N+M
# stack frames consume O(N+M) space.

from __future__ import print_function
from typing import Optional


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


class Solution:
    def mergeTwoLists_I(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        # iterative soln
        sentinel = Node(-1)

        prev = sentinel
        while list1 and list2:
            if list1.value <= list2.value:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        prev.next = list1 if list1 else list2

        return sentinel.next

    def mergeTwoLists_R(self, list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
        # recursive solution
        if not list1:
            return list2
        elif not list2:
            return list1
        elif list1.value < list2.value:
            list1.next = self.mergeTwoLists_R(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_R(list1, list2.next)
            return list2


def main():
    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(4)
    l1.next.next.next = Node(9)

    l2 = Node(1)
    l2.next = Node(3)
    l2.next.next = Node(4)

    print("Nodes of first list are: ", end='')
    l1.print_list()
    print("Nodes of second list are: ", end='')
    l2.print_list()

    sol = Solution()
    result = sol.mergeTwoLists_I(l1, l2)
    print("[Iterative Solution] Nodes of combined lists are: ", end='')
    result.print_list()

    l1 = Node(1)
    l1.next = Node(2)
    l1.next.next = Node(4)
    l1.next.next.next = Node(9)

    l2 = Node(1)
    l2.next = Node(3)
    l2.next.next = Node(4)

    result = sol.mergeTwoLists_R(l1, l2)
    print("[Recursive Solution] Nodes of combined lists are: ", end='')
    result.print_list()


main()
