# Given a set of distinct numbers, find all of its permutations.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/B8R83jyN3KY
# Leetcode https://leetcode.com/problems/permutations/
# Solution https://leetcode.com/problems/permutations/solution/
# Time Complexity We know that there are a total of N! permutations of a set with ‘N’ numbers. In the algorithm above, we are iterating through all of these permutations
# with the help of the two ‘for’ loops. In each iteration, we go through all the current permutations to insert a new number in them on line 17.
# To insert a number into a permutation of size ‘N’ will take O(N), which makes the overall time complexity of our algorithm O(N*N!).
# Space Complexity All the additional space used by our algorithm is for the result list and the queue to store the intermediate permutations. If you see closely, at any
# time, we don’t have more than N! permutations between the result list and the queue. Therefore the overall space complexity to store N! permutations each
# containing N elements will be O(N*N!).


def generate_permutations(nums):
    result = []
    generate_permutations_recursive(nums, 0, [], result)
    return result


def generate_permutations_recursive(nums, index, current_permutation, result):
    if index == len(nums):
        result.append(current_permutation)
    else:
        for i in range(len(current_permutation)+1):
            new_premutation = list(current_permutation)
            new_premutation.insert(i, nums[index])
            generate_permutations_recursive(
                nums, index+1, new_premutation, result)


def main():
    print("Here are all the permutations: " +
          str(generate_permutations([1, 3, 5])))


main()
