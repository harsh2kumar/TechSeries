# Find middle of a given SLL
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3j5GD3EQMGM
# Refer to https://leetcode.com/problems/middle-of-the-linked-list/
# Solution https://leetcode.com/problems/middle-of-the-linked-list/solution/
# Time Complexity: O(N)
# Space Complexity: O(1)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def find_middle_of_linked_list(head):
    slow, fast = head, head
    # in case of even nodes, fast will reach null
    # for that scenario, we need to make sure fast is not null
    # otherwise, code will error out when executing fast.next -> null.next
    while (fast is not None) and (fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next = Node(6)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))

    head.next.next.next.next.next.next = Node(7)
    print("Middle Node: " + str(find_middle_of_linked_list(head).value))


main()
