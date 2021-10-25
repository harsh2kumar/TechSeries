# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/mElknO5OKBO
# Leetcode https://leetcode.com/problems/3sum-smaller/
# Solution https://leetcode.com/problems/3sum-smaller/solution/
# Time Complexity Sorting the array will take O(N * logN). The search_pairs() function will take O(N^2). 
# As we are calling search_pairs() for every number in the input array, this means that overall search_triplets() will take O(N * logN + N^2)
# which is asymptotically equivalent to O(N^2)
# Space Complexity Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr)-2):
        count += search_pairs(arr, i+1, target-arr[i])
    return count
def search_pairs(arr, left, target):
    count = 0
    right = len(arr)-1
    while left<right:
        # found the triplet
        # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
        # left and right to get a sum less than the target sum
        if arr[left]+arr[right]<target:
            count += right-left
            left += 1
        else: 
            # we need a pair with a smaller sum
            right -= 1
    return count

def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
