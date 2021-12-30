# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# Return the linked list sorted as well.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/N0GQG1BnoqL
# Refer to https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Solution https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/solution/
# Time Complexity The time complexity is O(N)
# Space Complexity The space complexity is O(1) when using sentinel node

from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def remove_duplicates(lst):
    if lst.is_empty():
        return lst
    head = lst.get_head()
    # if LL is empty or contains one node
    if not head or not head.next_element:
        return head

    sentinel = Node(0)
    sentinel.next_element = head
    prev, cur = sentinel, head
    while cur:
        if cur.next_element and cur.data == cur.next_element.data:
            while cur.next_element and cur.data == cur.next_element.data:
                cur = cur.next_element
            prev.next_element = cur.next_element
        else:
            prev = prev.next_element
        cur = cur.next_element
        lst.head_node = sentinel.next_element
    return lst


def main():
    lst = LinkedList()
    lst.insert_at_head(5)
    lst.insert_at_head(4)
    lst.insert_at_head(4)
    lst.insert_at_head(3)
    lst.insert_at_head(3)
    lst.insert_at_head(2)
    lst.insert_at_head(1)

    lst.print_list()
    remove_duplicates(lst)
    lst.print_list()

    lst = LinkedList()
    lst.insert_at_head(3)
    lst.insert_at_head(2)
    lst.insert_at_head(1)
    lst.insert_at_head(1)
    lst.insert_at_head(1)
    lst.print_list()
    remove_duplicates(lst)
    lst.print_list()


main()
