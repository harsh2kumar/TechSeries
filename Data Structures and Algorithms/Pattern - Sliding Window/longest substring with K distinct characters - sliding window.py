# Given a string, find the longest substirng with atmost 'K' distinct characters.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/7XMlMEQPnnQ
# Leetcode https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# Solution https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/solution/
# Time Complexity O(N)
# Space Complexity O(1)


def longest_substring_with_k_distinct(str1, k):
    max_length, window_start = -1, 0
    char_freq = {}

    # try to extend the length of sliding window
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        char_freq[right_char] = char_freq.get(right_char, 0)+1

        # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
        while len(char_freq) > k:
            left_char = str1[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1  # shrink the window
        # calculate the max length of sliding window
        max_length = max(max_length, window_end-window_start+1)
    return max_length


def main():
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("cbbebi", 3)))
    print("Length of the longest substring: " +
          str(longest_substring_with_k_distinct("abcd", 4)))


main()
