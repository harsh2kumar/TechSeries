# Given the head of a linked list with even length, return the maximum twin sum of the linked list.
# Grokking
# Leetcode https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Solution https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/solution/
# Time Complexity: The runtime complexity of this solution is linear, O(n). Runtime complexity is based on the length of the linked lists.
# Space Complexity: The space complexity is O(1), since we use constant space for storing max_twin_sum and pointers.
from __future__ import print_function
from typing import Optional


class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()


class Solution:
    def pairSum(self, head: Optional[Node]) -> int:
        def rev_ll(head):
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev

        # find the middle of LL
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        reversed_second_half = rev_ll(mid)

        ptr1, ptr2 = head, reversed_second_half
        max_twin_sum = 0
        while ptr1 and ptr2:
            max_twin_sum = max(max_twin_sum, ptr1.val+ptr2.val)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return max_twin_sum


def main():
    l1 = Node(5)
    l1.next = Node(4)
    l1.next.next = Node(2)
    l1.next.next.next = Node(1)

    l2 = Node(4)
    l2.next = Node(2)
    l2.next.next = Node(2)
    l2.next.next.next = Node(3)

    l3 = Node(1)
    l3.next = Node(100000)

    sol = Solution()

    print("Nodes of first list are: ", end='')
    l1.print_list()
    print("Maximum Twin Sum is: ", sol.pairSum(l1))

    print("Nodes of second list are: ", end='')
    l2.print_list()
    print("Maximum Twin Sum is: ", sol.pairSum(l2))

    print("Nodes of third list are: ", end='')
    l3.print_list()
    print("Maximum Twin Sum is: ", sol.pairSum(l3))


main()
