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
    word_len = len(word)
    abbreviation_queue = deque()
    abbreviation_queue.append(AbbreviatedWord(list(), 0, 0))

    while abbreviation_queue:
        ab_word = abbreviation_queue.popleft()
        if ab_word.start == word_len:
            if ab_word.count != 0:
                ab_word.string.append(str(ab_word.count))
            result.append("".join(ab_word.string))
        else:
            # continue abbreviating by incrementing the current abbreviation count
            abbreviation_queue.append(AbbreviatedWord(
                list(ab_word.string), ab_word.start+1, ab_word.count+1))
            # restart abbreviating, add current abbreviation count to string value, increment start value
            if ab_word.count != 0:
                ab_word.string.append(str(ab_word.count))
            new_word = list(ab_word.string)
            new_word.append(word[ab_word.start])
            abbreviation_queue.append(
                AbbreviatedWord(new_word, ab_word.start+1, 0))
    return result


def main():
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
          str(generate_generalized_abbreviation("code")))


main()
