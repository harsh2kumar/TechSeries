
# Given an array with positive numbers and a positive target number, find all of its contiguous subarrays whose product is less than the target number.
# Leetcode https://leetcode.com/problems/subarray-product-less-than-k/
# Solution https://leetcode.com/problems/subarray-product-less-than-k/solution
# Time Complexity The main for-loop managing the sliding window takes O(N). left can only be incremented at most N times
# Space Complexity We store result, product, left & right variables. So the Space Complexity is O(1)

def find_subarrays_count(arr, target):
    if target <= 1: return 0
    result = 0
    product = 1
    left = 0
    for right in range(len(arr)):
        product *= arr[right]
        while product>=target:
            product /= arr[left]
            left += 1
        result += right-left+1
    return result


def main():
  print(find_subarrays_count([2, 5, 3, 10], 30))
  print(find_subarrays_count([8, 2, 6, 5], 50))
  print(find_subarrays_count([1, 2, 3], 0))


main()