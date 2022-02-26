# Design a data structure that supports adding new words and finding if a string matches any previously added string.
# Grokking
# Leetcode https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Solution https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Time Complexity O(M) to build the trie where M is total number of characters in products. For each prefix we find its representative node in O(len(prefix)) and dfs
# to find at most 3 words which is an O(1) operation. Thus the overall complexity is dominated by the time required to build the trie.
# Space Complexity O(26n)=O(n). Here n is the number of nodes in the trie. 26 is the alphabet size. Space required for output is O(m) where m is the length of the
# search word.
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
