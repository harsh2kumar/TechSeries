# Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words 
# exactly once without any overlapping of words.
# It is given that all words are of the same length.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N8nMBvDQJ0m
# Leetcode https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Solution https://leetcode.com/problems/find-all-anagrams-in-a-string/solution/
# Time Complexity O(N*M*Len) where ‘N’ is the number of characters in the given string, ‘M’ is the total number of words, and ‘Len’ is the length of a word.
# Space Complexity O(M+N), where M is the total number of words and N is the total number of characters in the given string


def find_word_concatenation(str1, words):
    result_indices = []
    if len(words) == 0 or len(words[0]) == 0:
        return result_indices
    words_count, word_len = len(words), len(words[0])
    words_freq = {}
    for word in words:
        words_freq[word] = words_freq.get(word, 0) + 1

    # try to find all the words in the given string
    for i in range(len(str1)-word_len*words_count+1):
        words_seen = {}
        for j in range(words_count):
            next_word_index = i + j*word_len

            word = str1[next_word_index:next_word_index+word_len]
            
            # break if current word is not present in given word list
            if word not in words_freq:
                break

            words_seen[word] = words_seen.get(word, 0 ) + 1
            
            # break if freq of current word is higher than in given word list
            if words_seen[word] > words_freq[word]:
                break

            if j+1 == words_count:
                result_indices.append(i)
    return result_indices
def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))

main()
