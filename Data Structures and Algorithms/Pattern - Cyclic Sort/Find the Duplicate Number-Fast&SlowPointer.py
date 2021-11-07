# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. The array has only one duplicate but it can be repeated multiple times.
# Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3wEkKy6Pr9A
# Leetcode https://leetcode.com/problems/find-the-duplicate-number/
# Solution https://leetcode.com/problems/find-the-duplicate-number/solution
# Time Complexity The time complexity of the above algorithm is O(n).
# Space Complexity The algorithm runs in constant space O(1).


def find_duplicate(nums):
    slow, fast = nums[0], nums[nums[0]]
    # find if cycle exists
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]

    return find_beginning_cycle(find_cycle_length(slow, nums), nums)


def find_cycle_length(slow, nums):
    current = nums[nums[slow]]
    cycle_length = 1
    while current != nums[slow]:
        current = nums[current]
        cycle_length += 1
    return cycle_length


def find_beginning_cycle(cycle_length, nums):
    ptr1, ptr2 = nums[0], nums[0]

    while cycle_length > 0:
        ptr2 = nums[ptr2]
        cycle_length -= 1
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1


def main():
    print(find_duplicate([1, 4, 4, 3, 2]))
    print(find_duplicate([2, 1, 3, 3, 5, 4]))
    print(find_duplicate([2, 4, 1, 4, 4]))


main()
