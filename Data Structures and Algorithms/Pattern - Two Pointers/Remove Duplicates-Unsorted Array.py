# Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; after removing the duplicates in-place return the length of the subarray that has no duplicate in it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/mEEA22L5mNA
# Leetcode https://leetcode.com/problems/remove-element/
# Solution https://leetcode.com/problems/remove-element/solution/
# Time Complexity The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def remove_element(arr, key):
    # using Two-Pointer Search like mechanism
    # we copy our non-key member and then increase it by 1
    
    next_element = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_element] = arr[i]
            next_element += 1
    return next_element



def main():
    print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
    print(remove_element([2, 11, 2, 2, 1], 2))
    
main()
