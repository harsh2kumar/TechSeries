# Given an array, find the longest substring with distinct characters
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/YMzBx1gE5EO
# Leetcode https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Solution https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/
# Time Complexity O(N)
# Space Complexity O(K), where K is the number of distinct characters in the string


def non_repeat_substring(str1):
    char_map = {}
    window_start, max_length = 0, 0
    
    # try to extend the range [windowStart, windowEnd]
    for window_end in range(len(str1)):
        # find the current character
        # if the map already contains the 'right_char', shrink the window from the beginning so that
        # we have only one occurrence of 'right_char'
        right_char = str1[window_end]
        # if current character is in char map
        if right_char in char_map:
            # this is tricky; in the current window, we will not have any 'right_char' after its previous index
            # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
            window_start = max(window_start, char_map[right_char]+1)
        # store the latest index of current character
        char_map[right_char] = window_end
        # remember the max length
        max_length = max(max_length, window_end-window_start+1)
    # print(window_start, window_end)
    return max_length


def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbcdeaf")))


main()