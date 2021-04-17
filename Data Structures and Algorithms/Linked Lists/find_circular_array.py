# Find whether given array has a cycle in it
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/NE67J9YMj3m
# Refer to https://leetcode.com/problems/circular-array-loop/
# Solution https://leetcode.com/problems/circular-array-loop/solution - at the time of solving this question, a solution didn't exist
# Time Complexity: O(N^2)
# O(N) time complexity by remembering number which have been visited previously but resulted in no-cycle condition
# Space Complexity: O(1)


def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        # determine the direction - forward or backward
        is_forward = arr[i] >= 0
        slow, fast = i, i

        # if slow or fast becomes -1, we cannot find a cycle for this number
        while True:
            # move slow pointer
            slow = find_next_index(arr, is_forward, slow)
            # move fast pointer
            fast = find_next_index(arr, is_forward, fast)

            # if fast is valid move it forward
            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)

            # break condition
            # either of slow or fast becomes invalid
            # slow and fast pointer meet -> cycle in array established
            if slow == -1 or fast == -1 or slow == fast:
                break
        # if a valid cycle is found, return True
        if slow != -1 and slow == fast:
            return True
    # if no cycle is found, for all elements of the array then return False
    return False


def find_next_index(arr, is_forward, current_index):
    # find direction from current index
    direction = arr[current_index] >= 0

    # if the direction changes in the middle of cycle then its not acceptable
    if is_forward != direction:
        return -1

    # cyclic array
    next_index = (current_index+arr[current_index]) % len(arr)

    # one-element cycle is not accepted
    if next_index == current_index:
        return -1

    return next_index


def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))
    print(circular_array_loop_exists([3, 1, 2]))


main()
