from TrieNode import TrieNode


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()  # root

    # function to obtain index of char from 0 to 25
    def get_index(self, t):
        return ord(t)-ord('a')
    # function to insert a key in trie

    def insert(self, key):
        if key is None:
            return False

        key = key.lower()  # keys are stored in lower case
        current = self.root

        # iterate over each letter in key
        # if letter exists, go down a level
        # otherwise create a new TrieNode and go down a level
        for letter in key:
            index = self.get_index(letter)
            # insert character
            if current.children[index] is None:
                current.children[index] = TrieNode(letter)
                print(letter, " inserted")
            # go down one level
            current = current.children[index]
        current.is_end_word = True
        print("Key: ", key, " inserted\n")

    # Function to search a given key in Trie
    def search(self, key):
        if not key:
            return False

        key = key.lower()
        current = self.root

        # Iterate over each letter in the key
        # If the letter doesn't exist, return False
        # If the letter exists, go down a level
        # We will return true only if we reach the leafNode and
        # have traversed the Trie based on the length of the key

        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]
        if current is not None and current.is_end_word is True:
            return True
        return False


# Input keys (use only 'a' through 'z')
keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]
res = ["Not present in trie", "Present in trie"]

t = Trie()
print("Keys to insert:\n", keys)

# Construct Trie
for words in keys:
    t.insert(words)

# Search for different keys
print("the --- " + res[1] if t.search("the") else "the --- " + res[0])
print("these --- " + res[1] if t.search("these") else "these --- " + res[0])
print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])
print("b --- " + res[1] if t.search("b") else "b --- " + res[0])
