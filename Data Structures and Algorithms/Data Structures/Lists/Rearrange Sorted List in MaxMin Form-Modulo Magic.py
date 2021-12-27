# Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number,
# the 1st index will have the smallest, and the 2nd index will have second-largest, and so on. In other words, all the even-numbered indices will have the
# largest numbers in the list in descending order and the odd-numbered indices will have the smallest numbers in ascending order.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/N7lg89p3Yo2
# Leetcode
# Solution
# Time Complexity Since this algorithm only traverses over the list once, it’s in linear time, O(n).
# Space Complexity The space complexity is O(1).

# using O(1) space
# it fails if array has negative values
def max_min(lst):
    if len(lst) <= 0:
        return []
    min_index, max_index = 0, len(lst)-1
    max_val = lst[-1]+1
    for i in range(len(lst)):
        if i % 2 == 0:
            lst[i] += (lst[max_index] % max_val)*max_val
            max_index -= 1
        else:
            lst[i] += (lst[max_index] % max_val)*max_val
            min_index += 1
    for i in range(len(lst)):
        lst[i] //= max_val
    return lst


print(max_min([1, 2, 3, 4, 5, 6]))
print(max_min([-10, -1, 1, 1, 1, 1]))  # fails for negative values
print(max_min([1, 2, 3, 4, 5, 6, 7]))
print(max_min([1, 2, 3, 4, 5]))
print(max_min([]))
print(max_min([1, 1, 1, 1, 1]))
