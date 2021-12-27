# Implement a function find_second_maximum(lst) which returns the second largest element in the list.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/7DxxOz72RO8
# Leetcode
# Solution
# Time Complexity Since this algorithm only traverses over the list twice, it’s in linear time, O(n).
# Space Complexity The space complexity is O(1).


def find_second_maximum(lst):
    if len(lst) < 2:
        return
    # initialize to -inf
    max_no, second_max_no = float('-inf'), float('-inf')
    for ele in lst:
        # update the max_no if max_no value found
        if ele > max_no:
            second_max_no = max_no
            max_no = ele
        # check if it is the second_max_no and not equal to max_no
        if ele > second_max_no and ele != max_no:
            second_max_no = ele
    if second_max_no == float('-inf'):
        return
    return second_max_no


print(find_second_maximum([9, 2, 3, 6]))
