# Given a string and a pattern, find starting index of all permutation of the pattern in the string
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/xl2g3vxrMq3
# Leetcode https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Solution https://leetcode.com/problems/find-all-anagrams-in-a-string/solution/
# Time Complexity O(N+M)
# Space Complexity O(M), where M is the number of distinct characters in given pattern


def find_string_anagrams(str1, pattern):
    char_frequency_map = {}
    window_start, matched = 0, 0
    anagram_index_list = []

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
        if matched == len(char_frequency_map):
            anagram_index_list.append(window_start)

        # if window_end is bigger than length of pattern then start shrinking the window
        if window_end >= len(pattern)-1:
            left_char = str1[window_start]
            window_start += 1
            if left_char in char_frequency_map:
                # if freq of char is currently zero then remove one match
                # since moving window_start will affect frequency of that character
                if char_frequency_map[left_char] == 0:
                    matched -= 1
                char_frequency_map[left_char] += 1
    return anagram_index_list


def main():
    print(find_string_anagrams("oidbcaf", "abc"))
    print(find_string_anagrams("odicf", "dc"))
    print(find_string_anagrams("bcdxabcdy", "bcdyabcdx"))
    print(find_string_anagrams("aaacb", "abc"))
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))
    print(find_string_anagrams("aaaaaa", "aa"))


main()
