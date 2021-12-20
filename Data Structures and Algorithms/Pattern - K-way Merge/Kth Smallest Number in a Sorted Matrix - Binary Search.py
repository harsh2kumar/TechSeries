# Given an N * N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/x1NJVYKNvqz
# Leetcode https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# Solution https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solution/
# Time Complexity The Binary Search could take O(log(max-min )) iterations where ‘max’ is the largest and ‘min’ is the smallest element in the matrix
# and in each iteration we take O(N) for counting, therefore, the overall time complexity of the algorithm will be O(N*log(max-min)).
# Space Complexity The algorithm runs in constant space O(1).


def find_Kth_smallest(matrix, k):
    n = len(matrix)
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) / 2
        smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        if count < k:
            start = larger  # search higher
        else:
            end = smaller  # search lower

    return start


def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            # as matrix[row][col] is bigger than the mid, let's keep track of the
            # smallest number greater than the mid
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            # as matrix[row][col] is less than or equal to the mid, let's keep track of the
            # biggest number less than or equal to the mid
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1

    return count, smaller, larger


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 4], [2, 5]], 2)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[-5]], 1)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))

    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)))
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[1, 2], [1, 3]], 1)))


main()
