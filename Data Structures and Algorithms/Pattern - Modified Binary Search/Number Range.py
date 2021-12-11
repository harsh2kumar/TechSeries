# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’
# will be the first and last position of the ‘key’ in the array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/R1B78K9oBEz
# Leetcode https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Solution https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def find_range(arr, key):
    result = [-1, -1]
    result[0] = binary_search(arr, key, False)
    if result[0] != -1:  # if key is not in array, return [-1, -1]
        result[1] = binary_search(arr, key, True)
    return result


def binary_search(arr, key, find_last_element):
    n = len(arr)
    start, end = 0, n-1
    key_pos = -1
    while start <= end:
        mid = start+(end-start)//2
        if key < arr[mid]:
            end = mid-1
        elif key > arr[mid]:
            start = mid+1
        else:
            key_pos = mid
            if find_last_element:  # find the first position of key
                start = mid+1
            else:  # find last position of key
                end = mid-1
    return key_pos


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


main()
