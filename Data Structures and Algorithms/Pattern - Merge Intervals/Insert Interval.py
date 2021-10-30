# Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce
# a list that has only mutually exclusive intervals.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/3jKlyNMJPEM
# Leetcode https://leetcode.com/problems/insert-interval/
# Solution https://leetcode.com/problems/insert-interval/solution/
# Time Complexity As we are iterating through all the intervals only once, the time complexity of the above algorithm is O(N),
# where ‘N’ is the total number of intervals.
# Space Complexity The space complexity of the above algorithm will be O(N)O(N) as we need to return a list containing all the merged intervals.


def insert(intervals, new_interval):
    merged = []
    i, start, end = 0, 0, 1
    # add all non-overlapping intervals before the new interval to result
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1
    # merge any valid subsequent with new interval
    while i < len(intervals) and intervals[i][start] < new_interval[end]:
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1
    # add merged interval to result
    merged.append(new_interval)
    # add any remaining non-overlapping intervals to result
    while i < len(intervals):
        merged.append(intervals[i])
        i+=1
    return merged


def main():
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " +
          str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " +
          str(insert([[2, 3], [5, 7]], [1, 4])))


main()
