class TrieNode:
    def __init__(self, char='') -> None:
        self.children = [None]*26  # This will store pointers to the children
        self.is_end_word = False  # true if the node represents the end of word
        self.char = char  # To store the value of a particular key
