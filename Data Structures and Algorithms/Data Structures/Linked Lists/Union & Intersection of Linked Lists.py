# Union and intersection are two of the most popular operations which can be performed on data sets. Now, you will be implementing them for linked lists!
# Let’s take a look at their definitions:
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/q209j6WD23R
# Leetcode
# Solution
# Time Complexity The time complexity is O(N)
# Space Complexity The space complexity is O(N)

from LinkedList import LinkedList
from Node import Node


def union(list1, list2):
    # Return other List if one of them is empty
    if (list1.is_empty()):
        return list2
    elif (list2.is_empty()):
        return list1

    start = list1.get_head()

    # Traverse the first list till the tail
    while start.next_element:
        start = start.next_element

    # Link last element of first list to the first element of second list
    start.next_element = list2.get_head()
    list1.remove_duplicates()
    return list1


def intersection(list1, list2):

    result = LinkedList()
    current_node = list1.get_head()

    # Traversing list1 and searching in list2
    # insert in result if the value exists
    while current_node is not None:
        value = current_node.data
        if list2.search(value) is not None:
            result.insert_at_head(value)
        current_node = current_node.next_element

    # Remove duplicates if any
    result.remove_duplicates()
    return result


ulist1 = LinkedList()
ulist2 = LinkedList()
ulist1.insert_at_head(8)
ulist1.insert_at_head(22)
ulist1.insert_at_head(15)

print("List 1")
ulist1.print_list()

ulist2.insert_at_head(21)
ulist2.insert_at_head(14)
ulist2.insert_at_head(7)

print("List 2")
ulist2.print_list()

new_list = union(ulist1, ulist2)

print("Union of list 1 and 2")
new_list.print_list()

ilist1 = LinkedList()
ilist2 = LinkedList()

ilist1.insert_at_head(14)
ilist1.insert_at_head(22)
ilist1.insert_at_head(15)

ilist2.insert_at_head(21)
ilist2.insert_at_head(14)
ilist2.insert_at_head(15)

lst = intersection(ilist1, ilist2)
print("Intersection of list 1 and 2")
lst.print_list()
