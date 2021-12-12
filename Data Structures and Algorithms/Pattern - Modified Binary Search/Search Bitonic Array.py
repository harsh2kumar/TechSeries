# Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically
# increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in
# the array arr[i] != arr[i+1]. Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/7n3BlOvqW0r
# Leetcode
# Solution
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def search_bitonic_array(arr, key):
    # find max elment index
    max_index = find_max_index(arr)
    key_index = binary_search(arr, key, 0, max_index)
    if key_index != -1:
        return key_index
    return binary_search(arr, key, max_index+1, len(arr)-1)


def find_max_index(arr):
    # find max element index of bitonic array
    start, end = 0, len(arr)-1
    while start < end:
        mid = start+(end-start)//2
        if arr[mid] < arr[mid+1]:
            start = mid+1
        else:
            end = mid
    # loop ends when start==end
    return start

# perform order-agnostic binary search


def binary_search(arr, key, start, end):
    is_increasing = arr[start] < arr[end]
    while start <= end:
        mid = start+(end-start)//2
        if key == arr[mid]:
            return mid
        if is_increasing:  # ascending order
            if key < arr[mid]:
                end = mid-1
            else:
                start = mid+1
        else:  # descending order
            if key > arr[mid]:
                end = mid-1
            else:
                start = mid+1
    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


main()
