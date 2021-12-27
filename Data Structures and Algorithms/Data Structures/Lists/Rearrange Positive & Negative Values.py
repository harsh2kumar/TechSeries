# Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at
# the right of the list. Note that it is not necessary to maintain the sorted order of the input list. Consider 0 as
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/qVN4327EA0p
# Leetcode
# Solution
# Time Complexity Since this algorithm only traverses over the list once, it’s in linear time, O(n).
# Space Complexity The space complexity is O(1).


def rearrange(lst):
    first_positive_num_index = 0
    for i in range(len(lst)):
        if lst[i] < 0:
            # swap the negative elements with index 0 and so on...
            lst[first_positive_num_index], lst[i] = lst[i], lst[first_positive_num_index]
            first_positive_num_index += 1
    return lst


print(rearrange([10, -1, 20, 4, 5, -9, -6]))
