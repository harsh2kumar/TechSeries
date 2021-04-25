# Given two baskets, put maximum number of contiguous subarray fruits in each basket. The only restriction is that each basket can have only one type of fruit.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/Bn2KLlOR0lQ
# Leetcode https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
# Solution https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/solution/
# Time Complexity O(N)
# Space Complexity O(1)


def fruits_into_baskets(fruits):
    return longest_substring_with_k_distinct(fruits, 2)

def longest_substring_with_k_distinct(fruits, k):
    fruit_frequecy = {}
    window_start, window_len = 0, -1

    for window_end in range(len(fruits)):
        fruit_frequecy[fruits[window_end]] = fruit_frequecy.get(fruits[window_end], 0) + 1
        while len(fruit_frequecy)>k:
            fruit_frequecy[fruits[window_start]] -= 1
            if fruit_frequecy[fruits[window_start]] == 0:
                del fruit_frequecy[fruits[window_start]]
            window_start += 1
        window_len = max(window_len, window_end-window_start+1)
    return window_len
    
def main():
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " +
          str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
