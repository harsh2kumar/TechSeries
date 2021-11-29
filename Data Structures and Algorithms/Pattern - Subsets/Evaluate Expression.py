# Given an expression containing digits and operations (+, -, *), find all possible ways in which the expression can be evaluated by grouping the numbers
# and operators using parentheses.
# Grokking https://www.educative.io/courses/grokking-the-coding-interview/N0Q3PKRKMPz
# Leetcode https://leetcode.com/problems/different-ways-to-add-parentheses/
# Solution https://leetcode.com/problems/different-ways-to-add-parentheses/solution/
# Time Complexity The overall time complexity of the algorithm will be O(N*2^N). Check Notion for accurately calculating overall complexity.
# Space Complexity All the additional space used by our algorithm is for the output list. Since we can have a total of O(2^N) combinations, the space complexity
# of our algorithm is O(N*2^N).

def diff_ways_to_evaluate_expression(input):
    result = []
    if "+" not in input and "-" not in input and "*" not in input:
        result.append(int(input))
    else:
        for i in range(len(input)):
            char = input[i]
            # if there is an operand, break the equation into two parts and make recursive calls
            if not char.isdigit():
                left_part = diff_ways_to_evaluate_expression(input[0:i])
                right_part = diff_ways_to_evaluate_expression(input[i+1:])
                # evaluate the expressions
                for part1 in left_part:
                    for part2 in right_part:
                        if char == "+":
                            result.append(part1+part2)
                        elif char == "-":
                            result.append(part1-part2)
                        elif char == "*":
                            result.append(part1*part2)
    return result


def main():
    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " +
          str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
