# Find whether given SLL is a palindrome
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/qAo438WozV7
# Refer to https://leetcode.com/problems/reorder-list/
# Solution https://leetcode.com/problems/reorder-list/

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    if head is None or head.next is None:
        return head

    # find middle of the SLL
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # create a copy for first half of SLL and reverse second half of the SLL
    head_first_half = head
    head_second_half = reverse(slow)

    # iterate through the two halves and rearrange the SLL
    while head_first_half and head_second_half:
        temp = head_first_half.next
        # Towards the end, last node's next node will be set to None
        head_first_half.next = head_second_half
        head_first_half = temp

        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp

    # set the next node of last node to None
    if head_first_half is not None:
        head_first_half.next = None

    return head


def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)

    head.print_list()
    reorder(head)
    head.print_list()


main()
