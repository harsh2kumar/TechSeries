# Find whether given SLL is a palindrome
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/JERG3q0p912
# Refer to https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/
# Solution https://leetcode.com/problems/palindrome-linked-list/

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def is_palindromic_linked_list(head):
    # base case
    # if SLL is empty or contains one node, then
    # it's a palindrome
    if (head is None or head.next is None):
        return True

    # find middle of SLL
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse second half of the SLL
    head_reverse_second_half = reverse(slow)

    # to return SLL to its original ordering, store the head of reversed second_half
    # TBD - Why does re-reversing work?
    # the node before the middle node still points to the middle node
    # store head of reversed second half to revert this half of SLL later
    copy_head_reverse_second_half = head_reverse_second_half
    # compare the first and second half
    while head is not None and head_reverse_second_half is not None:
        if head.value != head_reverse_second_half.value:
            break  # not a palindrome
        head = head.next
        head_reverse_second_half = head_reverse_second_half.next

    # revert the reverse of the second half
    reverse(copy_head_reverse_second_half)
    # we cannont have and condition here because head won't point to None
    if head is None or head_reverse_second_half is None:  # if both halves match
        return True

    return False


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
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
