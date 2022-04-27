# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# Grokking
# Leetcode https://leetcode.com/problems/contains-duplicate/
# Solution https://leetcode.com/problems/contains-duplicate/solution/
# Time Complexity  O(n). We do contains() and add() for n times and each operation takes constant time.
# Space Complexity O(n). The space used by a hash table is linear with the number of elements in it.


from collections import Counter, defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # optimization
        # return False if lenght of strings differs
        if len(s) != len(t):
            return False

        # sorting the string
        # return sorted(s) == sorted(t)

        # using single hashmap to store frequency of all chars in s
        # char_freq = Counter(s)
        # for char in t:
        #     char_freq[char] -= 1
        #     if char_freq[char] == 0:
        #         del char_freq[char]
        # if len(char_freq) == 0:
        #     return True
        # return False

        # using single hashmap, but increasing and decreasing count of characters at the
        # same time
        char_freq = defaultdict(int)
        for i in range(len(s)):
            char_freq[s[i]] += 1
            char_freq[t[i]] -= 1
            if char_freq[s[i]] == 0:
                del char_freq[s[i]]
            if char_freq[t[i]] == 0:
                del char_freq[t[i]]
        if len(char_freq) == 0:
            return True
        return False


sol = Solution()

print("anagram, nagaram: ", sol.isAnagram("anagram", "nagaram"))
print("rat, car: ", sol.isAnagram("rat", "car"))
