# Find whether given SLL has a cycle
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N7rwVyAZl6D
# Refer to https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/
# Solution https://leetcode.com/problems/linked-list-cycle/

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    """
    Return true if there is a cycle in the linked list. Otherwise, return false.
    """
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


def find_cycle_length(head: ListNode) -> int:
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return calculate_cycle_length(slow)
    return 0


def calculate_cycle_length(slow: ListNode) -> int:
    curr = slow
    cycle_length = 0
    while True:
        curr = curr.next
        cycle_length += 1
        if curr == slow:
            break
    return cycle_length


def main():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    # print("LinkedList has cycle: " + str(has_cycle(head)))

    # head.next.next.next.next.next.next = head.next.next
    # print("LinkedList has cycle: " + str(has_cycle(head)))

    # head.next.next.next.next.next.next = head.next.next.next
    # print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(find_cycle_length(head)))


main()
