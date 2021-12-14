# For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N0yqGR18jND
# Leetcode https://leetcode.com/problems/complement-of-base-10-integer/
# Solution https://leetcode.com/problems/complement-of-base-10-integer/solution/
# Time Complexity Since, wThe time complexity of our algorithm will be O(b), where ‘b’ is the total bits in the given number.
# Space Complexity The algorithm runs in constant space O(1).


def calculate_bitwise_complement(num):
    if num == 0:
        return 1
    bit_count, n = 0, num
    while n > 0:
        n = n >> 1
        bit_count += 1
    all_bits_set = pow(2, bit_count)-1
    return all_bits_set ^ num


def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(0)))


main()
