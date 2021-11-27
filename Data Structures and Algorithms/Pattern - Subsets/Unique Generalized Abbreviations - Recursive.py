# Given a word, write a function to generate all of its unique generalized abbreviations.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/NEOZDEg5PlN
# Leetcode https://leetcode.com/problems/generalized-abbreviation/
# Solution https://leetcode.com/problems/generalized-abbreviation/solution/
# Time Complexity The overall time complexity of the algorithm will be O(N*2^N). Check Notion for accurately calculating overall complexity.
# Space Complexity All the additional space used by our algorithm is for the output list. Since we can have a total of O(2^N) combinations, the space complexity
# of our algorithm is O(N*2^N).

from collections import deque


class AbbreviatedWord:
    def __init__(self, string, start, count):
        self.string = string  # list storing characters of the string
        self.start = start  # start index in word
        self.count = count  # abbreviation count in word


def generate_generalized_abbreviation(word):
    result = []
    generate_generalized_abbreviation_recursive(word, list(), 0, 0, result)
    return result


def generate_generalized_abbreviation_recursive(word, ab_word, start, count, result):

    if start == len(word):
        if count != 0:
            ab_word.append(str(count))
        result.append("".join(ab_word))
    else:
        # continue abbreviating by incrementing the current abbreviation count
        generate_generalized_abbreviation_recursive(
            word, list(ab_word), start+1, count+1, result)
        # restart abbreviating, add current abbreviation count to string value, increment start value
        if count != 0:
            ab_word.append(str(count))
        new_word = list(ab_word)
        new_word.append(word[start])
        generate_generalized_abbreviation_recursive(
            word, list(new_word), start+1, 0, result)


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))


main()
