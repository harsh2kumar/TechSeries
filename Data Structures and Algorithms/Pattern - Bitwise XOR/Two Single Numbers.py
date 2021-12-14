# In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N7VMDGgr9Vm
# Leetcode https://leetcode.com/problems/single-number-iii/
# Solution https://leetcode.com/problems/single-number-iii/solution/
# Time Complexity Since, wThe time complexity of our algorithm will be O(N), where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def find_single_numbers(nums):
    num1xnum2 = 0
    for num in nums:
        num1xnum2 ^= num
    rightmost_set_bit = 1

    # find the rightmost set bit
    while rightmost_set_bit & num1xnum2 == 0:
        rightmost_set_bit = rightmost_set_bit << 1

    num1, num2 = 0, 0
    for num in nums:
        if rightmost_set_bit & num != 0:  # bit is not set
            num1 ^= num
        else:
            num2 ^= num
    return [num1, num2]


def main():
    print('Single numbers are:' +
          str(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5])))
    print('Single numbers are:' + str(find_single_numbers([2, 1, 3, 2])))


main()
