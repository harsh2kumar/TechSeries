# Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3j7zEJzL2y9
# Leetcode https://leetcode.com/problems/flipping-an-image/
# Solution https://leetcode.com/problems/flipping-an-image/solution/
# Time Complexity The time complexity of this solution is O(n) as we iterate through all elements of the input.
# Space Complexity The algorithm runs in constant space O(1).


from typing import MutableSet


def flip_an_invert_image(matrix):
    row_len = len(matrix)
    for row in matrix:
        for i in range((row_len+1)//2):
            row[i], row[row_len-i-1] = row[row_len-i-1] ^ 1, row[i] ^ 1
    return matrix


def main():
    print(flip_an_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_an_invert_image(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


main()
