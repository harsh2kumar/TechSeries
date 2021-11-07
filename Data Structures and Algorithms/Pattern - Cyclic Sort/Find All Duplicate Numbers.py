# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times.
# Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RLw1Pjk1GQ0
# Leetcode https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Solution https://leetcode.com/problems/find-all-duplicates-in-an-array/solution
# Time Complexity The time complexity of the above algorithm is O(n).
# Space Complexity The algorithm runs in constant space O(1).


def find_all_duplicates(nums):
    i, duplicate_nums = 0, []
    while i < len(nums):
        j = nums[i]-1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i+=1
    for i in range(len(nums)):
        if nums[i]!=i+1:
            duplicate_nums.append(nums[i])
    return duplicate_nums

def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()
