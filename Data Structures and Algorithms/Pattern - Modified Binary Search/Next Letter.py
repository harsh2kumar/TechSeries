# Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/g2w6QPBA2Nk
# Leetcode https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Solution https://leetcode.com/problems/find-smallest-letter-greater-than-target/solution/
# Time Complexity Since, we are reducing the search range by half at every step, this means that the time complexity of our algorithm will be O(logN)
# where ‘N’ is the total elements in the given array.
# Space Complexity The algorithm runs in constant space O(1).


def search_next_letter(letters, key):
    n = len(letters)
    start, end = 0, n-1

    while start <= end:
        # calculate the middle of the current range
        mid = start + (end-start)//2
        if key < letters[mid]:
            end = mid-1
        else:  # key>=letters[mid]
            start = mid+1
    # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
    return letters[start % n]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
