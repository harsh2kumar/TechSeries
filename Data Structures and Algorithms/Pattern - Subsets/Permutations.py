# Given a set of distinct numbers, find all of its permutations.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B8R83jyN3KY
# Leetcode https://leetcode.com/problems/permutations/
# Solution https://leetcode.com/problems/permutations/solution/
# Time Complexity We know that there are a total of N! permutations of a set with ‘N’ numbers. In the algorithm above, we are iterating through all of these permutations
# with the help of the two ‘for’ loops. In each iteration, we go through all the current permutations to insert a new number in them on line 17.
# To insert a number into a permutation of size ‘N’ will take O(N), which makes the overall time complexity of our algorithm O(N*N!).
# Space Complexity All the additional space used by our algorithm is for the result list and the queue to store the intermediate permutations. If you see closely, at any
# time, we don’t have more than N! permutations between the result list and the queue. Therefore the overall space complexity to store N! permutations each
# containing N elements will be O(N*N!)O(N∗N!).

from collections import deque


def find_permutations(nums):
    result = []
    permutation_length = len(nums)  # determine length of permutation
    permutations = deque()
    permutations.append([])

    for num in nums:
        n = len(permutations)
        for _ in range(n):
            current_permutation = permutations.popleft()
            # add num at every position in current_permutation including after the last element
            for i in range(len(current_permutation)+1):
                new_permutation = list(current_permutation)
                new_permutation.insert(i, num)
                # if length matched permutation len, add it to result set at it contains all elements
                # otherwise add it to queue for further expansion
                if len(new_permutation) == permutation_length:
                    result.append(new_permutation)
                else:
                    permutations.append(new_permutation)
    return result


def main():
    print("Here are all the permutations: " +
          str(find_permutations([1, 3, 5])))


main()
