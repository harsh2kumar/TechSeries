# Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted
# in ascending or descending order. You should assume that the array can have duplicates. Write a function to return the index of the ‘key’ if it is present in
# the array, otherwise return -1.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/R8LzZQlj8lO
# Leetcode https://leetcode.com/problems/binary-search/
# Solution https://leetcode.com/problems/binary-search/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def binary_search(arr, key):
    start, end = 0, len(arr)-1
    # check if the array is ascending or descending
    is_ascending = arr[start] < arr[end]

    while start <= end:
        # calculate the middle of the current range
        mid = start + (end-start)//2
        if arr[mid] == key:
            return mid
        if is_ascending:  # ascending order
            if key < arr[mid]:
                end = mid - 1  # the 'key' can be in the first half
            else:  # key > arr[mid]
                start = mid + 1  # the 'key' can be in the second half
        else:  # descending order
            if key > arr[mid]:
                end = mid - 1  # the 'key' can be in the first half
            else:  # key < arr[mid]
                start = mid + 1  # the 'key' can be in the second half
    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


main()
