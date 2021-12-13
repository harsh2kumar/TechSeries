# In a non-empty array of integers, every number appears twice except for one, find that single number.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RLPGq6Vx0YY
# Leetcode https://leetcode.com/problems/missing-number/
# Solution https://leetcode.com/problems/missing-number/solution/
# Time Complexity Since, wThe time complexity of our algorithm will be O(N), where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def find_single_number(arr):
    x1 = 0

    for i in arr:
        x1 ^= i
    return x1


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))


main()
