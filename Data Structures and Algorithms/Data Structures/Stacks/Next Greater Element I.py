# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
# If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/JEP2nVGB4zv
# Leetcode https://leetcode.com/problems/next-greater-element-i/
# Solution https://leetcode.com/problems/next-greater-element-i/solution/
# Time Complexity Since this algorithm only traverses over the list once, it’s in linear time, O(n).
# Space Complexity The space complexity is O(n) because we store all elements in our map.


def nextGreaterElement(nums1, nums2):
    # find next greater element using stacks for nums2
    # store the results in a map
    # return the answer using map
    stack = []
    result = {}
    for i in range(len(nums2)-1, -1, -1):
        result[nums2[i]] = -1
        # remove all elements which are smalled than current
        # ele in nums2
        while stack and nums2[i] > stack[-1]:
            stack.pop()
        # top of stack should contain next greater element
        if stack:
            result[nums2[i]] = stack[-1]
        # push current element in stack
        stack.append(nums2[i])
    # populate next greater elements acc to nums1
    return [result[i] for i in nums1]


if __name__ == "__main__":
    print(nextGreaterElement([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7]))
    print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
    print(nextGreaterElement([2, 4], [1, 2, 3, 4]))
