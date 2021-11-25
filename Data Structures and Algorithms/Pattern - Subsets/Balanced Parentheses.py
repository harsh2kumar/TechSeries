# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/NEXBg8YA5A2
# Leetcode https://leetcode.com/problems/generate-parentheses/
# Solution https://leetcode.com/problems/generate-parentheses/solution/
# Time Complexity The overall time complexity of the algorithm will be O(N*2^N). Check Notion for accurately calculating overall complexity.
# Space Complexity All the additional space used by our algorithm is for the output list. Since we can have a total of O(2^N) combinations, the space complexity
# of our algorithm is O(N*2^N).

from collections import deque

# define class to maintain count of open and closed parenthesis for each string


class ParenthesisString:
    def __init__(self, string, open_parenthesis, closed_parenthesis):
        self.string = string
        self.open_parenthesis = open_parenthesis
        self.closed_parenthesis = closed_parenthesis


def generate_valid_parentheses(num):
    result = []
    parenthesis_queue = deque()
    parenthesis_queue.append(ParenthesisString("", 0, 0))
    while parenthesis_queue:
        # start with parenthesis substring
        parenthesis_string = parenthesis_queue.popleft()
        # if valid number of parenthesis are present, add it to the result
        if parenthesis_string.open_parenthesis == num and parenthesis_string.closed_parenthesis == num:
            result.append(parenthesis_string.string)
        # add parenthesis
        else:
            # check if open parenthesis can be added
            if parenthesis_string.open_parenthesis < num:
                parenthesis_queue.append(ParenthesisString(
                    parenthesis_string.string+"(", parenthesis_string.open_parenthesis+1, parenthesis_string.closed_parenthesis))
            # check if closed parenthesis can be added
            if parenthesis_string.closed_parenthesis < parenthesis_string.open_parenthesis:
                parenthesis_queue.append(ParenthesisString(
                    parenthesis_string.string+")", parenthesis_string.open_parenthesis, parenthesis_string.closed_parenthesis+1))
    return result


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
