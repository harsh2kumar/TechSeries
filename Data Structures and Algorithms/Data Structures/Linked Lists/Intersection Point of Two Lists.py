# Given the head nodes of two linked lists that may or may not intersect, find out if they do in fact intersect and return the point of intersection.
# Return null otherwise.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/Y5ZR6rxknx2
# Leetcode https://leetcode.com/problems/intersection-of-two-linked-lists/
# Solution https://leetcode.com/problems/intersection-of-two-linked-lists/solution/
# Time Complexity The time complexity is O(M+N), where M and N are the length of two lists respectively
# Space Complexity The space complexity is O(1)

from LinkedList import LinkedList
from Node import Node


def intersect(headA, headB):
    listA_len, listB_len = get_length(headA), get_length(headB)
    len_diff = abs(listA_len-listB_len)
    if listA_len >= listB_len:
        long_list = headA
        short_list = headB
    else:
        long_list = headB
        short_list = headA
    while len_diff:
        long_list = long_list.next_element
        len_diff -= 1
    while long_list:
        if long_list == short_list:
            return short_list
        long_list = long_list.next_element
        short_list = short_list.next_element
    return None


def get_length(head):
    list_length = 0
    while head:
        head = head.next_element
        list_length += 1
    return list_length


list_1 = LinkedList([13, 4])
list_2 = LinkedList([29, 23, 82, 11])
node1 = Node(12)
node2 = Node(27)

list_1.insert_at_tail(node1)
list_2.insert_at_tail(node2)

list_2. insert_at_tail(node1)

print("List 1: ", end="")
list_1.display()
print("List 2: ", end="")
list_2.display()

intersect_node = intersect(list_1.get_head(), list_2.get_head())
print("Intersect at " + str(intersect_node.data))
