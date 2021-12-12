# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.
# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1.
# You can assume that the given array does not have any duplicates.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RMPVM2Y4PW0
# Leetcode https://leetcode.com/problems/search-in-rotated-sorted-array/
# Solution https://leetcode.com/problems/search-in-rotated-sorted-array/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def search_rotated_array(arr, key):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = start+(end-start)//2
        if key == arr[mid]:
            return mid
        # array is rotated, hence after an element, both parts are in ascending order
        # first part of array is ascending
        elif arr[start] <= arr[mid]:
            # key is in first part
            if key >= arr[start] and key < arr[mid]:
                end = mid-1
            else:
                start = mid+1
        else:  # second part of array is in ascending order
            # key is in second part
            if key > arr[mid] and key <= arr[end]:
                start = mid+1
            else:
                end = mid-1
    # if element is not found in given array
    return -1


def main():
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))
    print(search_rotated_array([3, 1], 1))


main()
