# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/g7pBzR12YPl
# Leetcode https://leetcode.com/problems/backspace-string-compare/
# Solution https://leetcode.com/problems/backspace-string-compare/solution/
# Time Complexity The time complexity of the above algorithm will be O(M+N) where ‘M’ and ‘N’ are the lengths of the two input strings respectively.
# Space Complexity The algorithm runs in constant space O(1).


def backspace_compare(str1, str2):
    index1 = len(str1)-1
    index2 = len(str2)-1

    while index1 >= 0 or index2 >= 0:
        i1 = get_next_valid_char_index(str1, index1)
        i2 = get_next_valid_char_index(str2, index2)

        if i1 < 0 and i2 < 0:
            return True
        if i1 < 0 or i2 < 0:
            return False
        if str1[i1] != str2[i2]:
            return False
        index1 = i1-1
        index2 = i2-1
    return True


def get_next_valid_char_index(string, index):
    backspace_count = 0
    while index >= 0:
        if string[index] == "#":
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        index -= 1
    return index


def main():
    print(backspace_compare("xy#z", "xzz#"))
    print(backspace_compare("xy#z", "xyz#"))
    print(backspace_compare("xp#", "xyz##"))
    print(backspace_compare("xywrrmp", "xywrrmu#p"))


main()
