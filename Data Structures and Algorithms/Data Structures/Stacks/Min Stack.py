# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
# If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/JEP2nVGB4zv
# Leetcode https://leetcode.com/problems/min-stack/
# Solution https://leetcode.com/problems/min-stack/solution/
# Time Complexity Since this algorithm only traverses over the list once, it’s in linear time, O(n).
# Space Complexity The space complexity is O(n) because we store all elements in our map.


class MinStack:

    def __init__(self):
        self.min_stack = []
        self.main_stack = []

    def push(self, val: int) -> None:
        # push value into main stack
        # insert value in min_stack if its empty, as this will be the corresponding min value for
        # this element
        # check if value<top element in min_stack
        # if yes, insert the new min
        # else insert the top element of min stack again for
        # minimum of corresponding element in main stack
        self.main_stack.append(val)
        if not self.min_stack or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        # both stacks will have the same number of elements
        # as we'll be adding corresponding min for each element in
        # main stack
        if self.min_stack:
            self.min_stack.pop()
            return self.main_stack.pop()
        return None

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]
        return None

    def min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None


if __name__ == "__main__":
    stack = MinStack()
    stack.push(5)
    stack.push(0)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(0)
    print("Main stack:", stack.main_stack)
    print("Min stack:", stack.min_stack)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    stack.push(-2)
    print("Main stack:", stack.main_stack)
    print("Min stack:", stack.min_stack)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    print("Main stack:", stack.main_stack)
    print("Min stack:", stack.min_stack)
    print("Minimum value: " + str(stack.min()))
