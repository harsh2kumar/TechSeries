# Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/B8oZYWXRVG2
# Leetcode https://leetcode.com/problems/add-two-numbers/
# Solution https://leetcode.com/problems/add-two-numbers/solution/
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


def add_integers(integer1, integer2):
    result, last = None, None
    carry = 0

    while integer1 or integer2 or carry:
        num1 = 0 if not integer1 else integer1.value
        num2 = 0 if not integer2 else integer2.value

        _sum = num1 + num2 + carry
        right_digit = Node(_sum % 10)
        carry = _sum//10

        if not result:
            result = right_digit
        else:
            last.next = right_digit
        last = right_digit
        if integer1:
            integer1 = integer1.next
        if integer2:
            integer2 = integer2.next
    return result


def main():
    l1 = Node(1)
    l1.next = Node(0)
    l1.next.next = Node(9)
    l1.next.next.next = Node(9)

    l2 = Node(7)
    l2.next = Node(3)
    l2.next.next = Node(2)

    print("Nodes of first integer are: ", end='')
    l1.print_list()
    print("Nodes of second integer are: ", end='')
    l2.print_list()

    result = add_integers(l1, l2)
    print("Nodes of added integers are: ", end='')
    result.print_list()


main()
