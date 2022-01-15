# Implement the `total_words()` function which will find the total number of words in a trie.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/YVnAYQAgNpK
# Leetcode
# Solution
# Time Complexity For a trie with n number of nodes, the algorithm runs in O(n) because each node has to be traversed
# Space Complexity If the length of the longest word is h, the worst-case space complexity is O(h). In the worst case, we have to look at h consecutive levels
# of a trie for a character in the key being searched for. Thus, the stack will have h recursive calls.
from Trie import Trie
from TrieNode import TrieNode

# TrieNode => {children, is_end_word, char}


def total_words(root):
    # check for None instead of [if not root]
    # so that valid value of '0' is not missed
    if root is None:
        return 0
    result = 0
    # increment count if current character is marked as end_word
    if root.is_end_word:
        result += 1
    for child in root.children:
        # call recursively if child is not None
        if child is not None:
            result += total_words(child)
    return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()

for key in keys:
    trie.insert(key)

print(total_words(trie.root))
