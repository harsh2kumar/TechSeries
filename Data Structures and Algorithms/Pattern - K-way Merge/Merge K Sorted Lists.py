# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/Y5n0n3vAgYK
# Leetcode https://leetcode.com/problems/merge-k-sorted-lists/
# Solution https://leetcode.com/problems/merge-k-sorted-lists/solution/
# Time Complexity Since we’ll be going through all the elements of all arrays and will be removing/adding one element to the heap in each step, the time complexity
# of the above algorithm will be O(N*logK), where ‘N’ is the total number of elements in all the ‘K’ input arrays.
# Space Complexity The space complexity will be O(K) because, at any time, our min-heap will be storing one number from all the ‘K’ input arrays.
from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    # used for the min-heap
    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists):
    minheap = []
    # put the root of each list in the min heap
    for root in lists:
        heappush(minheap, root)
    # for creating LL of merged K lists
    # take the smallest(top) element form the min-heap and add it to the result
    # if the top element has a next element add it to the heap
    result_head, result_tail = None, None
    while minheap:
        node = heappop(minheap)
        if result_head is None:
            result_head, result_tail = node, node
        else:
            # increment tail pointer
            result_tail.next = node
            result_tail = result_tail.next
        if node.next:
            heappush(minheap, node.next)
    return result_head


def main():
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end='')
    while result is not None:
        print(str(result.value) + " ", end='')
        result = result.next


main()
