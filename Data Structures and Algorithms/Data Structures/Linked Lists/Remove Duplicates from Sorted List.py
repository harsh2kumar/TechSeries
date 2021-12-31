# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/N0GQG1BnoqL
# Refer to https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Solution https://leetcode.com/problems/remove-duplicates-from-sorted-list/solution/
# Time Complexity The time complexity is O(N)
# Space Complexity The space complexity is O(N), can be done in O(1) as well using sentinel node

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

    seen = set()
    cur, prev = head, head
    while cur:
        # if current node is unseen, add it to set
        # and update prev to point to same node as cur
        if cur.data not in seen:
            seen.add(cur.data)
            prev = cur
        else:
            prev.next_element = cur.next_element
        cur = cur.next_element
    return lst


def main():
    lst = LinkedList()
    lst.insert_at_head(7)
    lst.insert_at_head(7)
    lst.insert_at_head(7)
    lst.insert_at_head(22)
    lst.insert_at_head(14)
    lst.insert_at_head(21)
    lst.insert_at_head(14)
    lst.insert_at_head(7)

    lst.print_list()
    remove_duplicates(lst)
    lst.print_list()


main()
