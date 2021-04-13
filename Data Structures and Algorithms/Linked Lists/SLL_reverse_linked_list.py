# Reverse a given SLL inplace
# Refer to https://leetcode.com/problems/reverse-linked-list/ | https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1205/ 
# Solution https://leetcode.com/problems/reverse-linked-list/solution/
# Time Complexity: O(N)
# Space Complexity: O(1)

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        curr = self
        output = ""
        while curr:
            output += str(curr.value)+" "
            curr = curr.next
        return output


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
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Reversed Linked List: " + str(reverse(head)))

    # double reversing of LL doesn't work
    # reverse(head)
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)
    head.next.next.next.next.next = Node(2)
    print("Reversed Linked List: " + str(reverse(head)))


main()
