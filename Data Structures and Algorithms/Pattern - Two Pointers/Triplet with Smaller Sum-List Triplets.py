# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/mElknO5OKBO
# Leetcode https://leetcode.com/problems/3sum-smaller/
# Solution https://leetcode.com/problems/3sum-smaller/solution/
# Time Complexity Sorting the array will take O(N * logN). The search_pairs(), in this case, will take O(N^2); 
# the main while loop will run in O(N) but the nested for loop can also take O(N) - this will happen when the target sum is bigger than every triplet in the array.
# So, overall triplet_with_smaller_sum() will take O(N * logN + N^3), which is asymptotically equivalent to O(N^3).
# Space Complexity Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.


def triplet_with_smaller_sum(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr)-2):
        search_pairs(arr, i+1, target-arr[i], triplets)
    return triplets
def search_pairs(arr, left, target, triplets):
    first = left-1
    right = len(arr)-1
    while left<right:
        # found the triplet
        # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
        # left and right to get a sum less than the target sum
        if arr[left]+arr[right]<target:
            for i in range(right, left, -1):
                triplets.append([arr[first], arr[left], arr[i]])
            left += 1
        else: 
            # we need a pair with a smaller sum
            right -= 1
    return triplets

def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()
