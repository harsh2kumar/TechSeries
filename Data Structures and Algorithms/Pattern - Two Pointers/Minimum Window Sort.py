# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/gxk639mrr5r
# Leetcode https://leetcode.com/problems/3sum/
# Solution https://leetcode.com/problems/3sum/solution/
# Time Complexity Sorting the array will take O(N * logN). The search_pairs() function will take O(N).
# As we are calling search_pairs() for every number in the input array, this means that overall search_triplets() will take O(N * logN + N^2)
# which is asymptotically equivalent to O(N^2)
# Space Complexity Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.


def shortest_window_sort(arr):
    low, high = 0, len(arr)-1
    
    # find boundaries for candidate subarray
    while low<len(arr)-1 and arr[low]<=arr[low+1]:
        low += 1
    if low == len(arr)-1:
        return 0
    while high>0 and arr[high]>=arr[high-1]:
        high -= 1
    
    # expand boundaries of candidate subarray
    # elements from beginning greater than min_cand_subarray
    # elements from end smaller than max_cand_subarray        
    min_cand_subarray = float('inf')
    max_cand_subarray = -float('inf')

    for k in range(low, high+1):
        min_cand_subarray = min(min_cand_subarray, arr[k])
        max_cand_subarray = max(max_cand_subarray, arr[k])
    
    while low>0 and arr[low-1]>min_cand_subarray:
        low -= 1
    while high<len(arr)-1 and arr[high+1]<max_cand_subarray:
        high += 1
    
    return high-low+1

def main():
    print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
    print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
    print(shortest_window_sort([1, 2, 3]))
    print(shortest_window_sort([3, 2, 1]))
    print(shortest_window_sort([1, 3, 2, 2, 2]))


main()
