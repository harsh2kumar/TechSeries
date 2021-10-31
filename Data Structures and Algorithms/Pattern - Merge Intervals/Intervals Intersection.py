# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/JExVVqRAN9D
# Leetcode https://leetcode.com/problems/interval-list-intersections/
# Solution https://leetcode.com/problems/interval-list-intersections/solution/
# Time Complexity As we are iterating through both the lists once, the time complexity of the above algorithm is O(N + M), where ‘N’ and ‘M’ are
# the total number of intervals in the input arrays respectively.
# Space Complexity Ignoring the space needed for the result list, the algorithm runs in constant space O(1).


def merge(intervals_a, intervals_b):
    result = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        # check if intervals overlap and intervals_a[i]'s start time lies within the other intervals_b[j]
        a_intersects_b = intervals_a[i][start] >= intervals_b[j][start] and \
            intervals_a[i][start] <= intervals_b[j][end]
        # check if intervals overlap and intervals_a[i]'s start time lies within the other intervals_b[j]
        b_intersects_a = intervals_b[j][start] >= intervals_a[i][start] and \
            intervals_b[j][start] <= intervals_a[i][end]
        if a_intersects_b or b_intersects_a:
            result.append([max(intervals_a[i][start], intervals_b[j][start]),
                           min(intervals_a[i][end], intervals_b[j][end])])
        if intervals_a[i][end] <= intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return result


def main():
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
