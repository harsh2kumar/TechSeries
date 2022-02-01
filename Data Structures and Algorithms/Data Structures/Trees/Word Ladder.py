# Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord,
# or 0 if no such sequence exists.
# Grokking
# Leetcode https://leetcode.com/problems/word-ladder/
# Solution https://leetcode.com/problems/word-ladder/solution/
# Time Complexity The runtime complexity of this solution is O(m^2*n) where m is the size of word and n is total number of words.
# Space Complexity The space complexity of this solution is O(m^2*n) where m is the size of word and n is total number of words.


from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endword is not in dict or wordlist, beginword, endword are empty
        # return 0
        if (endWord not in wordList) or not beginWord or not endWord or not wordList:
            return 0

        # find length of word, its same for all words
        length = len(beginWord)

        # add generic forms of word to dictionary
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(length):
                intermediate_word = word[:i]+"*"+word[i+1:]
                all_combo_dict[intermediate_word].append(word)

        # maintain a queue for words
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}

        while queue:
            current_word, level = queue.popleft()

            for i in range(length):
                intermediate_word = current_word[:i]+"*"+current_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level+1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level+1))
                # reset the words
                all_combo_dict[intermediate_word] = []

        return 0


sol = Solution()
print(sol.ladderLength("hit", "cog", [
      "hot", "dot", "dog", "lot", "log", "cog"]))
