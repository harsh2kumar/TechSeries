# iven the head node of a singly linked list and an integer 'n', rotate the linked list by 'n'. 'n' can be negative as well.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/m7xO9QGvXZr
# Leetcode https://leetcode.com/problems/rotate-list/
# Solution https://leetcode.com/problems/rotate-list/solution/
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


def rotate(head, rotations):
    # optimization
    if any([not head, not head.next]):
        return head

    # calculate length of LL and find its last node
    last_node, length = head, 1

    while last_node.next:
        last_node = last_node.next
        length += 1
    # make the LL cyclic
    last_node.next = head
    # no need to do rotations equal to LL length, only the remainder nodes need to be skipped
    # python modulo operator autmatically handles negative values of rotations
    rotations %= length
    skip_length = length-rotations

    # skip to the last node of rotated list by jumping (skip length - 1) nodes
    last_node_of_rotated_list = head
    while skip_length > 0:
        head = head.next
        last_node = last_node.next
        skip_length -= 1
    last_node.next = None

    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of 3 rotated LinkedList are: ", end='')
    result.print_list()

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    result = rotate(head, -2)
    print("Nodes of -2 rotated LinkedList are: ", end='')
    result.print_list()


main()
