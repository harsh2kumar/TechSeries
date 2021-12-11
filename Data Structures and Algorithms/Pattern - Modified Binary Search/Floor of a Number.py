# Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’. The floor of the ‘key’
# will be the biggest element in the given array smaller than or equal to the ‘key’.
# Write a function to return the index of the floor of the ‘key’. If there isn’t a floor, return -1.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/qA5wW7R8ox7
# Leetcode https://leetcode.com/problems/search-insert-position/
# Solution https://leetcode.com/problems/search-insert-position/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def search_floor_of_a_number(arr, key):
    n = len(arr)
    start, end = 0, len(arr)-1
    # if key is smaller than first element in array, floor of key is not present in the array, return -1
    if key < arr[0]:
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
    # we are not able to find the element in the given array, so the next smaller number will be arr[end]
    return end


def main():
    print(search_floor_of_a_number([4, 6, 10], 6))
    print(search_floor_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_floor_of_a_number([4, 6, 10], 17))
    print(search_floor_of_a_number([4, 6, 10], -1))


main()
