# Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3wENz1N4WW9
# Leetcode https://leetcode.com/problems/reverse-linked-list/
# Solution https://leetcode.com/problems/reverse-linked-list/solution/
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


def reverse(head):
    # optimization if SLL is empty or contains just one node
    # return the head
    if head is None or head.next is None:
        return head
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

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse(head)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
