# Union and intersection are two of the most popular operations which can be performed on data sets. Now, you will be implementing them for linked lists!
# Let’s take a look at their definitions:
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/q209j6WD23R
# Leetcode
# Solution
# Time Complexity The time complexity is O(N)
# Space Complexity The space complexity is O(1)

from LinkedList import LinkedList
from Node import Node


def find_nth(lst, n):
    if (lst.is_empty()):
        return -1

    # Find Length of list
    length = lst.length()

    # Find the Node which is at (len - n) position from start
    current_node = lst.get_head()

    position = length - n

    if position < 0 or position > length:
        return -1

    count = 1

    while count <= position:
        current_node = current_node.next_element
        count += 1

    if current_node:
        return current_node.data
    return -1


lst = LinkedList()
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.insert_at_head(8)
lst.insert_at_head(22)
lst.insert_at_head(15)


lst.print_list()
print(find_nth(lst, 5))
print(find_nth(lst, 1))
print(find_nth(lst, 10))
