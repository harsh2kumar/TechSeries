# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/gxk639mrr5r
# Leetcode https://leetcode.com/problems/3sum/
# Solution https://leetcode.com/problems/3sum/solution/
# Time Complexity Sorting the array will take O(N * logN). The search_pairs() function will take O(N). 
# As we are calling search_pairs() for every number in the input array, this means that overall search_triplets() will take O(N * logN + N^2)
# which is asymptotically equivalent to O(N^2)
# Space Complexity Ignoring the space required for the output array, the space complexity of the above algorithm will be O(N) which is required for sorting.


def search_triplets(arr):
    triplets = []
    # need to sort the array for this to work, otherwise we can have duplicate elements anywhere in the array
    arr.sort()
    for i in range(len(arr)):
        # cannot do arr[i-1] != arr[i] and have search_pairs inside it instead of continue because we are including condition for i>0
        if i>0 and arr[i-1]==arr[i]:
            continue
        # need to pass left=i+1 coz target_sum is -i, so it cannot be the same
        search_pairs(arr, -arr[i], i+1, triplets)
    return triplets

def search_pairs(nums, target_sum, left, triplets):
    right = len(nums)-1
    while left<right:
        curr_sum = nums[left]+nums[right]
        if curr_sum == target_sum:
            triplets.append([-target_sum, nums[left], nums[right]])
            left += 1
            right -= 1
            # skip all duplicate elements
            while left<right and nums[left-1]==nums[left]:
                left += 1
            # skip all duplicate elements
            while left<right and nums[right]==nums[right+1]:
                right -= 1
        elif curr_sum<target_sum:
            left += 1
        else:
            right -= 1

def main():

    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))


main()
