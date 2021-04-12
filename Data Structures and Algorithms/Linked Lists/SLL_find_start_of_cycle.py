# Find whether given SLL has a cycle
# If it has a cycle, return the node otherwise return null
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N7pvEn86YrN
# Refer to https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
# Solution https://leetcode.com/problems/linked-list-cycle-ii/

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    fast, slow = head, head
    cycle_length = -1
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # cycle found
            cycle_length = calculate_cycle_length(slow)
            return find_beginning_cycle(head, cycle_length)
    # no cycle found
    return None


def calculate_cycle_length(slow):
    # find cycle length
    curr = slow
    cycle_length = 0
    while True:
        curr = curr.next
        cycle_length += 1
        if slow == curr:
            break
    return cycle_length


def find_beginning_cycle(head, cycle_length):
    pointer1, pointer2 = head, head
    while cycle_length > 0: # move pointer2 ahead by the length of the cycle
        pointer2 = pointer2.next
        cycle_length -= 1
    while pointer1 != pointer2: # node where the two pointers meet is the beginning of the cycle
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    
    # No cycle
    print("LinkedList cycle start: " + str(find_cycle_start(head)))

    # cyle begins at 3rd node
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    # cyle begins at 4th node
    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    # cyle begins at 1st node
    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
