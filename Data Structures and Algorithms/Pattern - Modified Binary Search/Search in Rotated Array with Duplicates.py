# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.
# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RMPVM2Y4PW0
# Leetcode https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# Solution https://leetcode.com/problems/search-in-rotated-sorted-array-ii/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity
# of our algorithm will be O(logN). However, since we only skip two numbers in case of duplicates instead of half of the
# numbers, the worst case time complexity will become O(N), where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def search_rotated_with_duplicates(arr, key):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = start+(end-start)//2
        if key == arr[mid]:
            return mid
        # check for duplicates
        # the only difference from the previous solution,
        # if numbers at indexes start, mid, and end are same, we can't choose a side
        # the best we can do, is to skip one number from both ends as key != arr[mid]
        if arr[start] == arr[mid] and arr[mid] == arr[end]:
            start += 1
            end -= 1
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
    # if the element is not present in given array
    return -1


def main():
    print(search_rotated_with_duplicates([3, 7, 3, 3, 3], 7))


main()
