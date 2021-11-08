# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RMZylvkGznR
# Leetcode modification: If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# Leetcode https://leetcode.com/problems/reverse-nodes-in-k-group/
# Solution https://leetcode.com/problems/reverse-nodes-in-k-group/solution/
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


def reverse_every_k_elements(head, k):
    # optimization
    if k <= 1 or not head:
        return head
    current, prev = head, None
    i, length = 0, 0
    # reverse every k-group sub list
    while True:
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
        # break when current is None
        if current is None:
            break
        # assign previous as last node of sub_list
        prev = last_node_of_sub_list

    return head


def reverse_every_k_elements_leetcode(head, k):
    # optimization
    if k <= 1 or not head:
        return head
    current, prev = head, None
    i, length = 0, 0
    # calculate length of LL for Leetcode modification
    while current:
        current = current.next
        length += 1
    to_traverse = length-length % k
    current = head
    nodes_traversed = 0
    # reverse every k-group sub list
    while True:
        # save last node of first part
        last_node_of_previous_part = prev
        # save last node of sub list, current becomes last node of sub list after its reversal
        # after reversing current will become last node of LL
        last_node_of_sub_list = current
        # reverse k-element sub list
        i, next = 0, None
        while current and i < k and nodes_traversed <= to_traverse:
            next = current.next
            current.next = prev
            prev = current
            current = next
            nodes_traversed += 1
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
        # break when current is None or remaining nodes<k
        if current is None or nodes_traversed > to_traverse:
            break
        # assign previous as last node of sub_list
        prev = last_node_of_sub_list

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
    result = reverse_every_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    result = reverse_every_k_elements_leetcode(head, 3)
    print("(Leetcode)- remaining non-multiples of k shouldn't be reversed")
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
