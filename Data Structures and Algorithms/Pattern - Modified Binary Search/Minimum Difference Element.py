# Given an infinite sorted array (or an array with unknown size), find if a given number ‘key’ is present in the array.
# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/mymvP915LY9
# Leetcode
# Solution
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def search_min_diff_element(arr, key):
    n = len(arr)
    if key < arr[0]:
        return arr[0]
    elif key > arr[n-1]:
        return arr[n-1]
    start, end = 0, n-1
    while start <= end:
        mid = start+(end-start)//2
        if key == arr[mid]:
            return arr[mid]
        elif key < arr[mid]:
            end = mid-1
        else:
            start = mid+1
    if arr[start]-key < key-arr[end]:
        return arr[start]
    return arr[end]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
