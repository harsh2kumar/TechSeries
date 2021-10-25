# Given an array containing 0s, 1s and 2s, sort the array in-place. You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s 
# to recreate the array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RMBxV6jz6Q0
# Leetcode https://leetcode.com/problems/sort-colors/
# Solution https://leetcode.com/problems/sort-colors/solution/
# Time Complexity The above algorithm’s time complexity will be O(N) as we are iterating the input array only once.
# Space Complexity The algorithm runs in constant space O(1).


def dutch_flag_sort(arr):
    # all elements < low are 0, and all elements > high are 2
    # all elements >=low<i are 1
    low, high = 0, len(arr)-1
    i=0

    while i<=high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            # arr[low], arr[i] = arr[i], arr[low]
            # increment 'i' and 'low'
            low += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else: # the case for arr[i] == 2
            # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            arr[i], arr[high] = arr[high], arr[i]
            # arr[high], arr[i] = arr[i], arr[high]
            high -= 1


def main():
    arr = [1, 0, 2, 1, 0]
    dutch_flag_sort(arr)
    print(arr)

    arr = [2, 2, 0, 1, 2, 0]
    dutch_flag_sort(arr)
    print(arr)


main()
