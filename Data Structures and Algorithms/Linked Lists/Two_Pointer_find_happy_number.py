# Find whether given number is a happy number
# If it is a happy number, return True otherwise return False
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/39q3ZWq27jM
# Refer to https://leetcode.com/problems/happy-number/
# Solution https://leetcode.com/problems/happy-number/

def find_happy_number(num):
    # Two Pointer approach
    # Time Complexity: O(logN)
    # Space Complexity: O(1)
    slow, fast = num, num
    while True:
        slow = find_sum_square(slow)  # move 1 step
        fast = find_sum_square(find_sum_square(fast))  # move 2 steps
        if fast == slow:  # found the cycle
            break
    return fast == 1  # check if cycle is stuck at 1
    
    # Hashset based approach
    # Time Complexity: O(logN)
    # Space Complexity: O(logN)
    # find if number has already been visited
    # If yes, return False
    # if number visited is 1, return True

    # all_nums, curr_num = set(), n
    # while True:
    #     curr_num = self.calculate_square_sum(curr_num)
    #     if curr_num is 1:
    #         return True
    #     elif curr_num in all_nums:
    #         return False
    #     else:
    #         all_nums.add(curr_num)


def find_sum_square(num: int) -> int:
    _sum = 0
    while num:
        digit = num % 10
        _sum += digit*digit
        num //= 10
    return _sum


def main():
    print(find_happy_number(23))  # happy number
    print(find_happy_number(12))  # unhappy number


main()
