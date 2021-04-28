# Given a string, find the longest substring with repeating characters given that you are allowed to make a maximum of 'k' replacements
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/R8DVgjq78yR
# Leetcode https://leetcode.com/problems/longest-repeating-character-replacement/
# Solution https://leetcode.com/problems/longest-repeating-character-replacement/solution/
# Time Complexity O(N)
# Space Complexity O(1), asymptotically equivalent to O(26) where 26 is the number of lowercase(grokking) or uppercase(leetcode) characters in the string


def length_of_longest_substring(str1, k):
    frequency_map = {}
    max_len, max_repeating_freq = 0, 0
    window_start = 0
    # Try to extend the range [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        frequency_map[right_char] = frequency_map.get(right_char, 0)+1
        max_repeating_freq = max(max_repeating_freq, frequency_map[right_char])
        # Current window size is from window_start to window_end, overall we have a letter which is
        # repeating 'max_repeat_letter_count' times, this means we can have a window which has one letter
        # repeating 'max_repeat_letter_count' times and the remaining letters we should replace.

        # if the remaining letters are more than 'k', it is the time to shrink the window as we
        # are not allowed to replace more than 'k' letters
        if (window_end-window_start+1-max_repeating_freq) > k:
            left_char = str1[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        max_len = max(max_len, window_end-window_start+1)
    return max_len


def main():
    print(length_of_longest_substring("aabccbb", 2))
    print(length_of_longest_substring("abbcb", 1))
    print(length_of_longest_substring("abccde", 1))
    print(length_of_longest_substring("aaccaaa", 1))


main()
