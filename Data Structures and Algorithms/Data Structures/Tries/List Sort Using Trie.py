# In this problem, you have to implement the sort_list() function which will sort the elements of a list of strings.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/qAmW7rmLQVy
# Leetcode
# Solution
# Time Complexity For a trie with n number of nodes, the algorithm runs in O(n) because each node has to be traversed
# Space Complexity If the length of the longest word is h, the worst-case space complexity is O(h). In the worst case, we have to look at h consecutive levels
# of a trie for a character in the key being searched for. Thus, the stack will have h recursive calls.
from Trie import Trie
from TrieNode import TrieNode

# TrieNode => {children, is_end_word, char}


def find_words_rec(root, word, result):
    # return if root is None
    # check for None instead of [if not root]
    # so that valid value of '0' is not missed
    if root is None:
        return
    word.append(root.char)
    # add word if current character is marked as end_word
    if root.is_end_word:
        result.append("".join(word))
    for child in root.children:
        # call recursively if child is not None
        if child is not None:
            find_words_rec(child, word, result)
    # bactrack and delete last char
    del word[-1]


def sort_list(arr):
    # return empty list if arr is empty
    if not arr:
        return []
    result = []
    trie = Trie()
    # insert all words in trie
    for key in arr:
        trie.insert(key)
    find_words_rec(trie.root, [], result)
    return result


keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
print(sort_list(keys))
