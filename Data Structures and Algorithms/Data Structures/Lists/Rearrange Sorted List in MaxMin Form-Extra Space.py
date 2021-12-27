# Implement a function called max_min(lst) which will re-arrange the elements of a sorted list such that the 0th index will have the largest number,
# the 1st index will have the smallest, and the 2nd index will have second-largest, and so on. In other words, all the even-numbered indices will have the
# largest numbers in the list in descending order and the odd-numbered indices will have the smallest numbers in ascending order.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/N7lg89p3Yo2
# Leetcode
# Solution
# Time Complexity Since this algorithm only traverses over the list once, it’s in linear time, O(n).
# Space Complexity The space complexity is O(N).

# using O(N) space
def max_min(lst):
    if len(lst) <= 0:
        return []
    result = []
    for i in range(len(lst)):
        # add max elements at even postions
        if i % 2 == 0:
            result.append(lst[len(lst)-(i+1)])
        # add min elements at odd postions
        else:
            result.append(lst[i])
    # if length of list is odd, add the middle element
    if len(lst) % 2 == 1:
        result.append(lst[len(lst)//2])
    return result


print(max_min([1, 2, 3, 4, 5, 6]))
print(max_min([-10, -1, 1, 1, 1, 1]))
print(max_min([1, 2, 3, 4, 5, 6, 7]))
print(max_min([1, 2, 3, 4, 5]))
print(max_min([]))
print(max_min([1, 1, 1, 1, 1]))
