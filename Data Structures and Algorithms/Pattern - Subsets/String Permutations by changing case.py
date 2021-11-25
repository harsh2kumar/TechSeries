# Given a string, find all of its permutations preserving the character sequence but changing case.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/xVlKmyX542P
# Leetcode https://leetcode.com/problems/letter-case-permutation/
# Solution https://leetcode.com/problems/letter-case-permutation/solution/
# Time Complexity Since we can have 2^N permutations (capitalized or lower-case letter) at the most and while processing each permutation we convert it into
# a character array, the overall time complexity of the algorithm will be O(N*2^N).
# Space Complexity All the additional space used by our algorithm is for the output list. Since we can have a total of O(2^N) permutations, the space complexity
# of our algorithm is O(N*2^N).


def find_letter_case_string_permutations(str):
    permuations = []
    permuations.append(str)
    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permuations)
            for j in range(n):
                chars = list(permuations[j])
                chars[i] = chars[i].swapcase()
                permuations.append("".join(chars))
    return permuations


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
