# We are given a linked list where the node has two pointers. The first is the regular next pointer. The second pointer is called arbitrary_pointer
# and it can point to any node in the linked list. Your job is to write code to make a deep copy of the given linked list. Here, deep copy means
# that any operations on the original list (inserting, modifying and removing) should not affect the copied list.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/q2gkBmWGjAG
# Leetcode https://leetcode.com/problems/copy-list-with-random-pointer/
# Solution https://leetcode.com/problems/copy-list-with-random-pointer/solution/
# Time Complexity The time complexity is O(N)
# Space Complexity The space complexity is O(N)

import random


class LinkedListNode:
    def __init__(self, value, next=None, arbitrary=None):
        self.data = value
        self.next = next
        self.arbitrary = arbitrary


def deep_copy_arbitrary_pointer(head):
    if head is None:
        return None

    current = head
    new_head = None
    new_prev = None
    ht = dict()

    # create copy of the linked list, recording the corresponding
    # nodes in hashmap without updating arbitrary pointer
    while current:
        new_node = LinkedListNode(current.data)

        # copy the old arbitrary pointer in the new node
        new_node.arbitrary = current.arbitrary

        if new_prev:
            new_prev.next = new_node
        else:
            new_head = new_node

        ht[current] = new_node

        new_prev = new_node
        current = current.next

    new_current = new_head

    # updating arbitrary pointer
    while new_current:
        if new_current.arbitrary:
            node = ht[new_current.arbitrary]

            new_current.arbitrary = node

        new_current = new_current.next

    return new_head


def create_random_list(length):
    head = LinkedListNode(random.randint(0, 100))
    cur = head
    for i in range(1, length):
        new_node = LinkedListNode(random.randint(0, 100))
        cur.next = new_node
        cur = cur.next
    return head


def create_linked_list_with_arb_pointers(length):
    head = create_random_list(length)
    v = []
    temp = head
    while temp:
        v.append(temp)
        temp = temp.next

    for i in range(0, len(v)):
        j = random.randint(0, len(v) - 1)
        p = random.randint(0, 100)
        if p < 75:
            v[i].arbitrary = v[j]

    return head


def print_with_arb_pointers(head):
    while head:
        print(str(head.data) + "(", end="")
        if head.arbitrary:
            print(head.arbitrary.data, end="")
        print(")", end="")
        head = head.next
        if head:
            print(", ", end="")


head = create_linked_list_with_arb_pointers(5)
print("Original list: ", end="")
print_with_arb_pointers(head)

head2 = deep_copy_arbitrary_pointer(head)
# head2 = deep_copy_arbitrary_pointer_same_list(head)
print("\nDeep copied list: ", end="")
print_with_arb_pointers(head2)

head = create_linked_list_with_arb_pointers(3)
print("\nChanged original list: ", end="")
print_with_arb_pointers(head)

print("\nUnchanged deep copied list: ", end="")
print_with_arb_pointers(head2)
