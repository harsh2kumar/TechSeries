# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/xoyL4q6ApNE
# Leetcode https://leetcode.com/problems/minimum-window-substring/
# Solution https://leetcode.com/problems/minimum-window-substring/solution/
# Time Complexity O(N+M)
# Space Complexity O(M), where M is the number of distinct characters in given pattern


def find_substring(str1, pattern):
    char_frequency_map = {}
    window_start, matched = 0, 0
    min_substr_len = float('inf')
    substr_start = 0
    for c in pattern:
        char_frequency_map[c] = char_frequency_map.get(c, 0)+1

    # expand the window
    for window_end in range(len(str1)):
        right_char = str1[window_end]

        # if character is in freq map, reduce its count
        # if freq for a char is 0, that means its permuation was matched in given window
        if right_char in char_frequency_map:
            char_frequency_map[right_char] -= 1
            if char_frequency_map[right_char] == 0:
                matched += 1

        # if matched and keys of char_frequency_map match, then permutation exists
        # shrink the window
        while matched == len(char_frequency_map):
            if min_substr_len > window_end-window_start+1:
                min_substr_len = window_end-window_start+1
                substr_start = window_start

            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency_map:
                if char_frequency_map[left_char] == 0:
                    matched -= 1
                char_frequency_map[left_char] += 1
    if min_substr_len > len(str1):
        return ""
    return str1[substr_start:substr_start+min_substr_len]


def main():
    print(find_substring("aabdec", "abc"))
    print(find_substring("abdbca", "abc"))
    print(find_substring("adcad", "abc"))
    print(find_substring("ADOBECODEBANC", "ABC"))
    print(find_substring("ab", "a"))

main()
