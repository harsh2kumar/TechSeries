# For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/NEXBg8YA5A2
# Leetcode https://leetcode.com/problems/generate-parentheses/
# Solution https://leetcode.com/problems/generate-parentheses/solution/
# Time Complexity The overall time complexity of the algorithm will be O(N*2^N). Check Notion for accurately calculating overall complexity.
# Space Complexity All the additional space used by our algorithm is for the output list. Since we can have a total of O(2^N) combinations, the space complexity
# of our algorithm is O(N*2^N).


def generate_valid_parentheses(num):
    result = []
    parenthesis_string = [0 for i in range(2*num)]
    generate_valid_parentheses_recursive(
        num, 0, parenthesis_string, 0, 0, result)
    return result


def generate_valid_parentheses_recursive(num, index, parenthesis_string, open_parenthesis, closed_parenthesis, result):
    if open_parenthesis == num and closed_parenthesis == num:
        result.append("".join(parenthesis_string))
    else:
        if open_parenthesis < num:
            parenthesis_string[index] = "("
            generate_valid_parentheses_recursive(
                num, index+1, parenthesis_string, open_parenthesis+1, closed_parenthesis, result)
        if closed_parenthesis < open_parenthesis:
            parenthesis_string[index] = ")"
            generate_valid_parentheses_recursive(
                num, index+1, parenthesis_string, open_parenthesis, closed_parenthesis+1, result)


def main():
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
          str(generate_valid_parentheses(3)))


main()
