# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B6XOq8KlkWo
# Leetcode https://leetcode.com/problems/4sum/
# Solution https://leetcode.com/problems/4sum/solution/
# Time Complexity Sorting the array will take O(N*logN). Overall searchQuadruplets() will take O(N * logN + N^3), which is asymptotically equivalent to O(N^3)
# Space Complexity Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.


def search_pairs(nums, first, second, target, quadruplets):
    left = second+1
    right = len(nums)-1
    while left < right:
        quad_sum = nums[first]+nums[second]+nums[left]+nums[right]
        if quad_sum == target:
            quadruplets.append(
                [nums[first], nums[second], nums[left], nums[right]])
            left += 1
            right -= 1
            # skip all duplicate elements
            while left < right and nums[left-1] == nums[left]:
                left += 1
            # skip all duplicate elements
            while left < right and nums[right] == nums[right+1]:
                right -= 1
        elif quad_sum < target:
            left += 1
        else:
            right -= 1


def search_quadruplets(arr, target):
    quadruplets = []
    # need to sort the array for this to work, otherwise we can have duplicate elements anywhere in the array
    arr.sort()
    for i in range(len(arr)-3):
        # cannot do arr[i-1] != arr[i] and have search_pairs inside it instead of continue because we are including condition for i>0
        if i > 0 and arr[i-1] == arr[i]:
            continue
        for j in range(i+1, len(arr)-2):
            if j > i+1 and arr[j-1] == arr[j]:
                continue
            # need to pass left=i+1 coz target_sum is -i, so it cannot be the same
            search_pairs(arr, i, j, target, quadruplets)
    return quadruplets


def main():
    print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
    print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))


main()
