# Implement a function right_rotate(lst, k) which will rotate the given list by k. This means that the right-most elements will appear at the left-most position
# in the list and so on. You only have to rotate the list by one element at a time.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/qVN4327EA0p
# Leetcode https://leetcode.com/problems/rotate-array/
# Solution https://leetcode.com/problems/rotate-array/solution/

# using extra space
# Time Complexity Since this algorithm only traverses over the list twice, it’s in linear time, O(n).
# Space Complexity The space complexity is O(n).

# using reverse
# Time Complexity Since this algorithm only traverses over the list twice, it’s in linear time, O(n).
# Space Complexity The space complexity is O(1).

# using extra space
# Time Complexity Since this algorithm only traverses over the list twice, it’s in linear time, O(n).
# Space Complexity The space complexity is O(n).

# using extra space
def right_rotate_extra_space(lst, k):
    if len(lst) <= 0:
        k = 0
    else:
        k %= len(lst)

    return lst[-k:]+lst[:-k]


def right_rotate_reverse(lst, k):
    if len(lst) <= 0:
        k = 0
    else:
        k %= len(lst)
    n = len(lst)
    # reverse all elements
    lst = reverse(lst, 0, n-1)
    # reverse first k elements
    lst = reverse(lst, 0, k-1)
    # reverse last k-n elements
    lst = reverse(lst, k, n-1)

    return lst


def right_rotate_cyclic_sort(lst, k):
    if len(lst) <= 0:
        k = 0
    else:
        k %= len(lst)
    n = len(lst)

    start, count = 0, 0
    while count < n:
        current_index, prev_val = start, lst[start]
        while True:
            # start swapping shifted index values with current index
            # recalculate current index in every iteration
            next_index = (current_index+k) % n
            lst[next_index], prev_val = prev_val, lst[next_index]
            current_index = next_index
            count += 1
            # if the original index is reached, break out of the loop
            if current_index == start:
                break
        start += 1
    return lst


def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums


# using extra space
print("Using extra space")
print(right_rotate_extra_space([10, 20, 30, 40, 50], abs(3)))
print(right_rotate_extra_space([], 1))
print(right_rotate_extra_space([1, 2, 3, 4, 5], 2))
print(right_rotate_extra_space([300, -1, 3, 0], 3))
print(right_rotate_extra_space([0, 0, 0, 2], 2))
print(right_rotate_extra_space(['13', 'a', 'Python'], 3))
print(right_rotate_extra_space(['right', 'rotate', 'python'], 4))

# using reverse
print("Using array reversal")
print(right_rotate_reverse([10, 20, 30, 40, 50], abs(3)))
print(right_rotate_reverse([], 1))
print(right_rotate_reverse([1, 2, 3, 4, 5], 2))
print(right_rotate_reverse([300, -1, 3, 0], 3))
print(right_rotate_reverse([0, 0, 0, 2], 2))
print(right_rotate_reverse(['13', 'a', 'Python'], 3))
print(right_rotate_reverse(['right', 'rotate', 'python'], 4))

# using cyclic dependency
print("Using cyclic dependency")
print(right_rotate_cyclic_sort([10, 20, 30, 40, 50], abs(3)))
print(right_rotate_cyclic_sort([], 1))
print(right_rotate_cyclic_sort([1, 2, 3, 4, 5], 2))
print(right_rotate_cyclic_sort([300, -1, 3, 0], 3))
print(right_rotate_cyclic_sort([0, 0, 0, 2], 2))
print(right_rotate_cyclic_sort(['13', 'a', 'Python'], 3))
print(right_rotate_cyclic_sort(['right', 'rotate', 'python'], 4))
