# Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing
# and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array
# arr[i] != arr[i+1].
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RMyRR6wZoYK
# Leetcode https://leetcode.com/problems/find-peak-element/
# Solution https://leetcode.com/problems/find-peak-element/solution/
# Leetcode https://leetcode.com/problems/peak-index-in-a-mountain-array/
# Solution https://leetcode.com/problems/peak-index-in-a-mountain-array/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def find_max_in_bitonic_array(arr):
    n = len(arr)
    start, end = 0, n-1
    while start < end:
        mid = start+(end-start)//2
        if arr[mid] < arr[mid+1]:  # increasing sequence
            start = mid+1
        elif arr[mid] > arr[mid+1]:  # decreasing sequence
            end = mid
    # loop exited when start=end
    return arr[start]


def main():
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))


main()
