# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. The ceiling of the ‘key’ will be the smallest
# element in the given array greater than or equal to the ‘key’.
# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/qA5wW7R8ox7
# Leetcode
# Solution
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def search_ceiling_of_a_number(arr, key):
    n = len(arr)
    start, end = 0, len(arr)-1
    # if key is bigger than the last element, key is not present in the array, return -1
    if key > arr[n-1]:
        return -1

    while start <= end:
        # calculate the middle of the current range
        mid = start + (end-start)//2
        # return index if key is found
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            end = mid-1
        elif arr[mid] < key:
            start = mid+1
    # return start index if key is not found
    # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
    # we are not able to find the element in the given array, so the next big number will be arr[start]
    return start


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


main()
