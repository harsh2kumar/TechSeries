# You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to execute but once a task has finished,
# it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals
# that the server needs to finish all tasks. If at any time the server can’t execute any task then it must stay idle.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B1gBkopEBzk
# Leetcode https://leetcode.com/problems/task-scheduler/
# Solution https://leetcode.com/problems/task-scheduler/solution/
# Time Complexity The time complexity of the above algorithm is O(N*logN).
# Space Complexity The space complexity will be O(N), as in the worst case, we need to store all the ‘N’ tasks in the HashMap.
from heapq import *
from collections import Counter


def schedule_tasks(tasks, k):
    interval_count = 0
    maxheap, waitlist = [], []

    # find frequency of all tasks
    task_freq = Counter(tasks)

    # insert tasks in maxheap
    for task, freq in task_freq.items():
        heappush(maxheap, (-freq, task))

    while maxheap:
        waitlist = []
        n = k+1  # try to execute as many as 'k+1' tasks from the max-heap
        while maxheap and n > 0:
            freq, task = heappop(maxheap)
            interval_count += 1
            if -freq > 1:
                # decrement the frequency and add to the waitList
                waitlist.append((freq+1, task))
            n -= 1
        # put all tasks in waiting list back on the heap
        for freq, task in waitlist:
            heappush(maxheap, (freq, task))
        #  if we don't execute all k+1 steps, then remaining n time needs to be added as idle time
        # we'll be having 'n' idle intervals for the next iteration
        if maxheap:
            interval_count += n
    return interval_count


def main():
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
          str(schedule_tasks(['a', 'b', 'a'], 3)))


main()
