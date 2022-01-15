# You have to implement the is_formation_possible() function which will find whether a given word can be formed by combining two words from a dictionary.
# We assume that all words are in lower case.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/39oYNJJqMwO
# Leetcode https://leetcode.com/problems/word-break/
# Solution https://leetcode.com/problems/word-break/solution/
# Time Complexity f the length of the average word in the dictionary is h, then the time taken for trie construction is O(m×h). Let the length of the word being
# searched be n. Then, the complexity for this turns out to be n^2. Hence, the total time complexity is O(mh + n ^ 2)
# Space Complexity If the length of the longest word is h, the worst-case space complexity is O(h). In the worst case, we have to look at h consecutive levels
# of a trie for a character in the key being searched for. Thus, the stack will have h recursive calls.

# TrieNode => {children, is_end_word, char}
from Trie import Trie
from TrieNode import TrieNode


# Create Trie => trie = Trie()
# TrieNode => {children, is_end_word, char}
# Insert a Word => trie.insert(key)
# Search a Word => trie.search(key) return true or false
# Delete a Word => trie.delete(key)

def is_formation_possible(dictionary, word):
    # base case
    if not dictionary:
        return len(word) == 0
    trie = Trie()
    for key in dictionary:
        trie.insert(key)
    # print("*"*50)
    current = trie.root
    # Iterate all the letters of the word
    for i in range(len(word)):
        # print(word[i])
        # get index of the character from Trie
        index = trie.get_index(word[i])
        # if prefix doesn't exist
        # return False
        if current.children[index] is None:
            return False
        # if first word is present in trie
        # search for second word
        elif current.children[index].is_end_word:
            # elif current.is_end_word:
            if trie.search(word[i+1:]):
                print(word[:i+1], word[i+1:])
                return True
        current = current.children[index]
    return False


keys = ["the", "hello", "there", "answer",
        "any", "educative", "world", "their", "abc"]
print(is_formation_possible(keys, "helloworld"))
