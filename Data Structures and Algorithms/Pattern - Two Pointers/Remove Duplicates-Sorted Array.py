# Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/mEEA22L5mNA
# Leetcode https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Solution https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/
# Time Complexity The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def remove_duplicates(arr):
    # using Two-Pointer Search like mechanism
    # Since the array is sorted, 
    # we copy our next_non_duplicate member and then increase it by 1
    if not arr:
        return 0
    i, next_non_duplicate = 1, 1

    while i<len(arr):
        if arr[next_non_duplicate-1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
        i+=1
    return next_non_duplicate



def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))
    
main()
