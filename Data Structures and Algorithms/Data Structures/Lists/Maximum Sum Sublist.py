# Given an unsorted list A, the maximum sum sub list is the sub list (contiguous elements) from A for which the sum of the elements is maximum.
# In this challenge, we want to find the sum of the maximum sum sub list. This problem is a tricky one because the list might have negative integers
# in any position, so we have to cater to those negative integers while choosing the continuous sublist with the largest positive values.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/qVN4327EA0p
# Leetcode https://leetcode.com/problems/maximum-subarray/
# Solution https://leetcode.com/problems/maximum-subarray/solution/
# Time Complexity The time complexity of O(N)
# Space Complexity The space complexity is O(1).

def find_max_sum_sublist(lst):
    # we use Kadane's algorithm to find the max sum subarray
    # the max sum at A[i] is the maximum of A[i] or the the Sum (A[i-1], A[i-2],..A[0] and A[i])
    # local_maximum at index i is the maximum of A[i] and the sum of A[i] and local_maximum at index i-1.
    if len(lst) <= 0:
        return 0
    curr_sum, max_sum = 0, 0
    for ele in lst[1:]:
        curr_sum = max(ele, curr_sum+ele)
        max_sum = max(max_sum, curr_sum)
    return max_sum


print("Sum of largest subarray: ", find_max_sum_sublist(
    [-4, 2, -5, 1, 2, 3, 6, -5, 1]))
print("Sum of largest subarray: ",
      find_max_sum_sublist([1, 2, -100, 100, 300]))
