from os import curdir, device_encoding
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

    # Recursive function to delete given key
    def delete_helper(self, key, current, length, level):
        deleted_self = False

        if key is None:
            print("key doesn't exist")
            return deleted_self

        # Base Case:
        # We have reached at the node which points
        # to the alphabet at the end of the key
        if level is length:
            # If there are no nodes ahead of this node in
            # this path, then we can delete this node
            print("Level is at length, we are at end")
            if current.children.count(None) == len(current.children):
                print("- Node", current.char, ": has no children, delete it")
                current = None
                deleted_self = True

            # If there are nodes ahead of current in this path
            # Then we cannot delete current. We simply unmark this as leaf
            else:
                print("- Node", current.char, ": has children, don't delete it")
                current.is_end_of_word = False
                deleted_self = False
        # We haven't reached end,
        # keep on calling recursively
        else:
            index = self.get_index(key[level])
            print("Traverse to ", key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(
                key, child_node, length, level+1)

            print("Returned from ", key[level], " as ", child_deleted)

            if child_deleted:
                # Setting children pointer to None as child is deleted
                print("- Delete link from ", current.char, " to ", key[level])
                current.children[index] = None

                # Case 3: word has common prefix
                # if current is end word then
                # current is part of another key
                # so, we cannot delete this node and its parent path nodes
                if current.is_end_word:
                    print("- - Don't delete node ", current.char, ": word end")
                    deleted_self = False

                # Case 2: word is prefix
                # If child_node is deleted and current has more children
                # then current must be part of another key
                # So, we cannot delete current Node
                elif current.children.count(None) != len(current.children):
                    print("- - Don't delete node",
                          current.char, ": has children")
                    deleted_self = False

                # Else we can delete current
                else:
                    print("- - Delete node", current.char, ": has no children")
                    current = None
                    deleted_self = True
            else:
                deleted_self = False
        return deleted_self

    # Function to delete given key from Trie
    def delete(self, key):
        if self.root is None or key is None:
            print("None key or empty Trie error")
            return
        print("\nDeleting: ", key)
        self.delete_helper(key, self.root, len(key), 0)


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

# Delete abc
t.delete("abc")
print("Deleted key \"abc\" \n")

print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])
