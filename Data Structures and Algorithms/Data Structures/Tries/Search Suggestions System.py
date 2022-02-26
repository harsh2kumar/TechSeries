# You are given an array of strings products and a string searchWord. Return a list of lists of the suggested products after each character of searchWord is typed.
# Grokking
# Leetcode https://leetcode.com/problems/search-suggestions-system/
# Solution https://leetcode.com/problems/search-suggestions-system/solution/
# Time Complexity O(M) to build the trie where M is total number of characters in products. For each prefix we find its representative node in O(len(prefix)) and dfs
# to find at most 3 words which is an O(1) operation. Thus the overall complexity is dominated by the time required to build the trie.
# Space Complexity O(26n)=O(n). Here n is the number of nodes in the trie. 26 is the alphabet size. Space required for output is O(m) where m is the length of the
# search word.
from typing import List


class TrieNode:
    def __init__(self, char=''):
        self.is_word = False  # this will be true if the character represents end of word
        self.children = [None]*26  # this stores pointers to children
        self.char = char  # store character


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.result_list = []

    def get_index(self, t):
        return ord(t)-ord('a')

    def insert(self, key):
        if key is None:
            return False
        key = key.lower()
        current = self.root

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
            current = current.children[index]
        current.is_word = True

    def dfsWithPrefix(self, node, word):
        if len(self.result_list) == 3:
            return
        if node.is_word:
            self.result_list.append(word)
        # run dfs on all possible paths
        for child in node.children:
            if child is not None:
                self.dfsWithPrefix(child, word+child.char)

    def startsWith(self, prefix):
        self.result_list = []
        if not prefix:
            return self.result_list
        prefix = prefix.lower()
        current = self.root
        # traverse the prefix now
        for letter in prefix:
            index = self.get_index(letter)
            if current.children[index] is None:
                return self.result_list
            current = current.children[index]
        # add all words in dfsWithPrefix
        self.dfsWithPrefix(current, prefix)
        return self.result_list


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)
        prefix, result = "", []
        for letter in searchWord:
            prefix += letter
            result.append(trie.startsWith(prefix))
        return result


sol = Solution()
print('["mobile","mouse","moneypot","monitor","mousepad"], "mouse": ', sol.suggestedProducts(
    ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
print('["havana"], "havana"": ', sol.suggestedProducts(["havana"], "havana"))
print('["bags","baggage","banner","box","cloths"], "bags": ', sol.suggestedProducts(
    ["bags", "baggage", "banner", "box", "cloths"], "bags"))
