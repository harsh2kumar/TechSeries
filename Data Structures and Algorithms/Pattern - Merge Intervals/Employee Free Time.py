# For ‘K’ employees, we are given a list of intervals representing each employee’s working hours. Our goal is to determine if there is a free interval
# which is common to all employees. You can assume that each list of employee working hours is sorted on the start time.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/RLwKZWgMJ1q
# Leetcode https://leetcode.com/problems/employee-free-time/
# Solution https://leetcode.com/problems/employee-free-time/solution
# Time Complexity The above algorithm’s time complexity is O(N*logK), where ‘N’ is the total number of intervals, and ‘K’ is the total number of employees.
# This is because we are iterating through the intervals only once (which will take O(N)), and every time we process an interval, we remove (and can insert)
# one interval in the Min Heap, (which will take O(logK)). At any time, the heap will not have more than ‘K’ elements.
# Space Complexity The space complexity of the above algorithm will be O(K) as at any time, the heap will not have more than ‘K’ elements.
from __future__ import print_function
from heapq import *


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, employee_index, interval_index):
        self.interval = interval
        self.employee_index = employee_index
        self.interval_index = interval_index

    def __lt__(self, other):
        # return value based on start of interval
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    if schedule is None:
        return []

    result, min_heap = [], []
    # insert first interval of all employees
    for i in range(len(schedule)):
        heappush(min_heap, EmployeeInterval(schedule[i][0], i, 0))

    previous_interval = min_heap[0].interval
    while min_heap:
        queue_top = heappop(min_heap)

        # if previous interval doesn't overlap with next interval, insert free interval
        if previous_interval.end<queue_top.interval.start:
            result.append(Interval(previous_interval.end, queue_top.interval.start))
            previous_interval = queue_top.interval
        # overlapping intervals, update previous interval if needed
        else:
            if previous_interval.end<queue_top.interval.end:
                previous_interval = queue_top.interval
        # add remaining interval's from an employee's schedule to min_heap
        employee_schedule = schedule[queue_top.employee_index]
        if len(employee_schedule)>queue_top.interval_index+1:
            heappush(min_heap, EmployeeInterval(employee_schedule[queue_top.interval_index+1], queue_top.employee_index, queue_top.interval_index+1))
    return result

def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
