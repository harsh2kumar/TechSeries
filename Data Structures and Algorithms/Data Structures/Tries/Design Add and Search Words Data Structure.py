# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Grokking
# Leetcode https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Solution https://leetcode.com/problems/design-add-and-search-words-data-structure/aolution/
# Time Complexity O(M) for the "well-defined" words without dots, where MM is the key length, and NN is a number of keys, and O(N⋅26^M) for the "undefined" words.
# That corresponds to the worst-case situation of searching an undefined word which is one character longer than all inserted keys.
# Space Complexity O(1) for the search of "well-defined" words without dots, and up to O(M) for the "undefined" words, to keep the recursion stack.
from typing import List


class TrieNode:
    def __init__(self, char=''):
        self.is_word = False
        self.children = [None]*26
        self.char = char


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def get_index(self, t):
        return ord(t)-ord('a')

    def addWord(self, word: str) -> None:
        if not word:
            return
        # convert to lowercase
        word = word.lower()
        current = self.root
        for letter in word:
            index = self.get_index(letter)
            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
            current = current.children[index]
        current.is_word = True

    def search(self, word: str) -> bool:
        if not word:
            return True
        current = self.root
        # print(word)

        def search_in_current(current, word):
            for i, letter in enumerate(word):
                if letter == ".":
                    for child in current.children:
                        if child is not None and search_in_current(child, word[i+1:]):
                            return True
                    return False
                else:
                    index = self.get_index(letter)
                    if current.children[index] is None:
                        return False
                    current = current.children[index]
            if current is not None and current.is_word:
                return True
            return False
        return search_in_current(current, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
sol = WordDictionary()
print(sol.addWord("bad"))
print(sol.addWord("dad"))
print(sol.addWord("mad"))
print(sol.search("pad"))
print(sol.search("bad"))
print(sol.search(".ad"))
print(sol.search("b.."))
