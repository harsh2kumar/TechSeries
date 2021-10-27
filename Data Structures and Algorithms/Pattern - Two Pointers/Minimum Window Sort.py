# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N8rOAP6Lmw6
# Leetcode https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Solution https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
# Time Complexity The time complexity of the above algorithm will be O(N).
# Space Complexity The algorithm runs in constant space O(1).


def shortest_window_sort(arr):
    low, high = 0, len(arr)-1

    # find boundaries for candidate subarray
    while low < len(arr)-1 and arr[low] <= arr[low+1]:
        low += 1
    if low == len(arr)-1:
        return 0
    while high > 0 and arr[high] >= arr[high-1]:
        high -= 1

    # expand boundaries of candidate subarray
    # elements from beginning greater than min_cand_subarray
    # elements from end smaller than max_cand_subarray
    min_cand_subarray = float('inf')
    max_cand_subarray = -float('inf')

    for k in range(low, high+1):
        min_cand_subarray = min(min_cand_subarray, arr[k])
        max_cand_subarray = max(max_cand_subarray, arr[k])

    while low > 0 and arr[low-1] > min_cand_subarray:
        low -= 1
    while high < len(arr)-1 and arr[high+1] < max_cand_subarray:
        high += 1

    return high-low+1


def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))
    print(shortest_window_sort([1, 3, 2, 2, 2]))


main()
