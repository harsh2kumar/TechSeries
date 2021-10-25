# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3YlQz7PE7OA
# Leetcode https://leetcode.com/problems/3sum-closest/
# Solution https://leetcode.com/problems/3sum-closest/solution/
# Time Complexity Sorting the array will take O(N * logN). Overall, the function will take O(N * logN + N^2)​​, which is asymptotically equivalent to O(N^2).
# Space Complexity The above algorithm’s space complexity will be O(N), which is required for sorting.


def triplet_sum_close_to_target(arr, target_sum):
    smallest_diff = float('inf')
    # need to sort the array for this to work, otherwise we can have duplicate elements anywhere in the array
    arr.sort()
    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1
        while(left<right):
            target_diff = target_sum - (arr[i]+arr[left]+arr[right])
            # we've found a triplet with an exact sum
            # return the sum of triplet
            if target_diff == 0:
                return target_sum
            # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
            # if target_diff=2 and smallest_diff=-2, we need to update smallest_diff to -2, since target_sum-smallest_diff will increase otherwise.
            # save the closest and the biggest difference
            elif (abs(target_diff)<abs(smallest_diff)) or (abs(target_diff)==abs(smallest_diff) and target_diff>smallest_diff):
                smallest_diff = target_diff
            if target_diff>0:
                # we need a triplet with a bigger sum
                left += 1
            else:
                # we need a triplet with a smaller sum
                right -= 1
    return target_sum-smallest_diff

def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()
