# Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/q2lZKgLm980
# Leetcode
# Solution
# Time Complexity: The time complexity of our algorithm will be O(N) where ‘N’ is the total number of nodes in the LinkedList.
# Space Complexity: We only used constant space, therefore, the space complexity of our algorithm is O(1).

from __future__ import print_function


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


def reverse_alternate_k_elements(head, k):
    # optimization
    if k <= 1 or not head:
        return head
    current, prev = head, None
    i = 0
    # reverse every k-group sub list
    while current:
        # save last node of first part
        last_node_of_previous_part = prev
        # save last node of sub list, current becomes last node of sub list after its reversal
        # after reversing current will become last node of LL
        last_node_of_sub_list = current
        # reverse k-element sub list
        i, next = 0, None
        while current and i < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            i += 1

        # connect with previous part
        # assign next for last node of previous part to reversed sub-list
        if last_node_of_previous_part:
            # previous is first node of sub-list after reversal
            last_node_of_previous_part.next = prev
        # head needs to be assigned as prev
        # we are changing head node of LL
        else:
            head = prev

        # assign last node of sub list
        # connect with last part
        if last_node_of_sub_list:
            last_node_of_sub_list.next = current
        # skip k-elements
        i = 0
        while current and i < k:
            prev = current
            current = current.next
            i += 1

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
