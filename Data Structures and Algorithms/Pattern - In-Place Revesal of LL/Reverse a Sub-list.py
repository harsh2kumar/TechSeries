# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/qVANqMonoB2
# Leetcode https://leetcode.com/problems/reverse-linked-list-ii/
# Solution https://leetcode.com/problems/reverse-linked-list-ii/solution/
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


def reverse_sub_list(head, p, q):
    # skip first p-1 nodes
    current, prev = head, None
    i = 0
    while current and i < p-1:
        prev = current
        current = current.next
        i += 1

    # save last node of first part
    last_node_of_first_part = prev
    # save last node of sub list, current becomes last node of sub list after its reversal
    # after reversing current will become last node of LL
    last_node_of_sub_list = current

    # reverse the sub list between p and q
    i, next = 0, None
    while current and i < q-p+1:
        next = current.next
        current.next = prev
        prev = current
        current = next
        i += 1

    # connect with first part
    # assign next for last node of first part to reversed sub-list
    if last_node_of_first_part:
        # previous is first node of sub-list after reversal
        last_node_of_first_part.next = prev
    # p=1, head needs to be assigned as prev
    # we are changing head node of LL
    else:
        head = prev

    # assign last node of sub list
    # connect with last part
    if last_node_of_sub_list:
        last_node_of_sub_list.next = current
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

#   head = Node(3)
#   head.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_sub_list(head, 1, 2)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
