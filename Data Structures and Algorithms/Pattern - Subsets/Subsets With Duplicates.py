# Given a set of numbers that might contain duplicates, find all of its distinct subsets.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/7npk3V3JQNr
# Leetcode https://leetcode.com/problems/subsets-ii/
# Solution https://leetcode.com/problems/subsets-ii/solution/
# Time Complexity Since, in each step, the number of subsets doubles as we add each element to all the existing subsets, therefore, we will have a total of O(2^N) subsets,
# where ‘N’ is the total number of elements in the input set. And since we construct a new subset from an existing set, therefore, the time complexity of the
# above algorithm will be O(N*2^N).
# Space Complexity All the additional space used by our algorithm is for the output list. Since we will have a total of O(2^N) subsets, and each subset can take
# up to O(N) space, therefore, the space complexity of our algorithm will be O(N*2^N).

def find_subsets(nums):
    # sort the numbers to handle duplicates
    nums.sort()
    subsets = []
    start_index, end_index = 0, 0
    # start by appending empty list
    subsets.append([])
    for i in range(len(nums)):
        start_index = 0
        if i > 0 and nums[i] == nums[i-1]:
            start_index = end_index+1
        end_index = len(subsets)-1
        for j in range(start_index, end_index+1):
            # create a new subset and append new number
            current_subset = list(subsets[j])
            current_subset.append(nums[i])
            subsets.append(current_subset)
    return subsets


def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()
