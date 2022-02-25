# Design a search autocomplete system for a search engine. Users may input a sentence (at least one word and end with a special character '#').
# Grokking
# Leetcode https://leetcode.com/problems/design-search-autocomplete-system/
# Solution https://leetcode.com/problems/design-search-autocomplete-system/solution/
# Time Complexity
# Space Complexity


from typing import List
from collections import defaultdict


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.search = ""
        self.history = defaultdict(int)
        for i in range(len(sentences)):
            self.history[sentences[i]] = times[i]
        self.matches = []

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.history[self.search] += 1
            self.search = ""
            self.matches = []
            return

        # search string is empty
        if not self.search:
            for sentence in self.history:
                if sentence[0] == c:
                    self.matches.append([sentence, self.history[sentence]])
            # sort by frequency and the first char
            self.matches.sort(key=lambda x: (-x[1], x[0]))
            self.matches = [x[0] for x in self.matches]
        # search for next character in the search string
        else:
            i = len(self.search)
            self.matches = [match for match in self.matches if len(
                match) > i and match[i] == c]
        self.search += c
        return self.matches[:3]


sol = AutocompleteSystem(
    ["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])
searches = [["i"], [" "], ["a"], ["#"]]
print("Search")
for search in searches:
    print(sol.input(search[0]))
