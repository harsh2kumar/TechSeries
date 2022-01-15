# There is a dictionary containing words from an alien language for which we don’t know the ordering of the alphabets. Write a method to find the correct order of
# the alphabets in the alien language. It is given that the input is a valid dictionary and there exists an ordering among its alphabets.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/R8AJWOMxw2q
# Leetcode https://leetcode.com/problems/alien-dictionary/
# Solution https://leetcode.com/problems/alien-dictionary/solution/
# Time Complexity The time complexity of the above algorithm will be O(V+E), where ‘V’ is the total number of tasks and ‘E’ is the total number of prerequisites in the graph.
# Space Complexity The space complexity will be O(V+E), since we are storing all of the prerequisites for each vertex in an adjacency list.
from Trie import Trie
from TrieNode import TrieNode

# TrieNode => {children, is_end_word, char}


def total_words(root):
    # check for None instead of [if not root]
    # so that valid value of '0' is not missed
    if root is None:
        return 0
    result = 0
    if root.is_end_word:
        result += 1
    for child in root.children:
        result += total_words(child)
    return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()

for key in keys:
    trie.insert(key)

print(total_words(trie.root))
