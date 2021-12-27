# Given two sorted lists, merge them into one list which should also be sorted.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/39Vv2YVxxVx
# Leetcode
# Solution
# Time Complexity In the worst-case, the second list has all the elements that are smaller than the elements of the first list. In this case, the complexity will be O(mn)O(mn).
# Space Complexity The space complexity is O(m).


def merge_arrays(lst1, lst2):
    # Creating 2 new variable to track the 'current index'
    ind1, ind2 = 0, 0
    # While both indices are less than the length of their lists
    while ind1 < len(lst1) and ind2 < len(lst2):
        # If the current element of list1 is greater
        # than the current element of list2
        if lst1[ind1] > lst2[ind2]:
            # insert list2's current index to list1
            lst1.insert(ind1, lst2[ind2])
            # increment indices
            ind1 += 1
            ind2 += 1
        else:
            ind1 += 1

    if ind2 < len(lst2):
        lst1.extend(lst2[ind2:])  # Append whatever is left of list2 to list1
    return lst1


print(merge_arrays([4, 5, 6], [-2, -1, 0, 7]))
