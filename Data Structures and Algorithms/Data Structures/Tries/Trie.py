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


# Input keys (use only 'a' through 'z')
keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]

t = Trie()
print("Keys to insert:\n", keys)

# Construct Trie
for words in keys:
    t.insert(words)
