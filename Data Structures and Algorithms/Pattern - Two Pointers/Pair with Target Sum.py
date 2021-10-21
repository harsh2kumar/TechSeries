# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/xog6q15W9GP
# Leetcode https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Solution https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/solution/
# Time Complexity The time complexity of the above algorithm will be O(N), where ‘N’ is the total number of elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def pair_with_targetsum(arr, target_sum):
    # using Two-Pointer Search like mechanism
    # Since the array is sorted, 
    # we increase our left pointer if sum of our elements is less than target sum
    # we decrease our right pointer if sum of our elements is greater than target sum
    left, right = 0, len(arr)-1
    while left<right:
        curr_sum = arr[left]+arr[right]
        if curr_sum == target_sum:
            return [left, right]
        if curr_sum<target_sum:
            left += 1
        else:
            right -= 1
    return []

def pair_with_targetsum_hashmap(arr, target_sum):
    # using HashMap based approach
    # Key - element
    # Value - index of element
    # if we have already seen target-num, we return current index and index of target-num from our dict
    nums_dict = {}
    for index, num in enumerate(arr):
        if target_sum-num in nums_dict:
            if index != nums_dict[target_sum-num]:
                return [index, nums_dict[target_sum-num]]
        nums_dict[num] = index
    return []

def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))
    print(pair_with_targetsum_hashmap([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum_hashmap([2, 5, 9, 11], 11))

main()
