# Given the head of a linked list, find all the values that appear more than once in the list and delete the nodes that have any of those values.
# Return the linked list after the deletions.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/N0GQG1BnoqL
# Refer to https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/
# Solution https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/solution/
# Time Complexity The time complexity is O(N)
# Space Complexity The space complexity is O(N)

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
    # calculate frequency of all elements
    freq_dict = {}
    cur = head
    while cur:
        freq_dict[cur.data] = freq_dict.get(cur.data, 0)+1
        cur = cur.next_element
    sentinel = Node(0)
    sentinel.next_element = head
    prev, cur = sentinel, head
    while cur:
        if freq_dict[cur.data] > 1:
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

    print()
    lst = LinkedList()
    lst.insert_at_head(3)
    lst.insert_at_head(2)
    lst.insert_at_head(1)
    lst.insert_at_head(1)
    lst.insert_at_head(1)
    lst.print_list()
    remove_duplicates(lst)
    lst.print_list()

    print()
    lst = LinkedList()
    lst.insert_at_head(2)
    lst.insert_at_head(3)
    lst.insert_at_head(2)
    lst.insert_at_head(1)
    lst.print_list()
    remove_duplicates(lst)
    lst.print_list()


main()
