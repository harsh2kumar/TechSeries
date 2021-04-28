# Given a string and a pattern, find if permutation of the pattern exists in string
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N0o9QnPLKNv
# Leetcode https://leetcode.com/problems/permutation-in-string/
# Solution https://leetcode.com/problems/permutation-in-string/solution/
# Time Complexity O(N)
# Space Complexity O(M), where M is the number of distinct characters in given pattern


def find_permutation(str1, pattern):
    char_frequency_map = {}
    window_start, matched = 0, 0

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
            return True

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
    return False


def main():
    print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
    print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
    print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
    print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()
