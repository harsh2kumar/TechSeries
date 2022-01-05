# Implement the function reverseK(queue, k) which takes a queue and a number “k” as input and reverses the first “k” elements of the queue.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/m7Mq9GR4omG
# Leetcode https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Solution https://leetcode.com/problems/evaluate-reverse-polish-notation/solution/
# Time Complexity Since this algorithm only traverses over the list once, it’s in linear time, O(n).
# Space Complexity The space complexity is O(n).


def evalRPN(tokens):
    stack = []
    for token in tokens:
        # check if string is numeric or contains a negative number
        if token.isnumeric() or (token.replace("-", "")).isnumeric():
            stack.append(int(token))
        else:
            # second operand is on the left side of operator
            op1, op2 = stack.pop(), stack.pop()
            if token == "+":
                stack.append(op2+op1)
            elif token == "*":
                stack.append(op2*op1)
            elif token == "/":
                # perform floating point division
                # typecast using int
                # the division should truncate towards zero
                stack.append(int(op2/op1))
            elif token == "-":
                stack.append(op2-op1)
    return stack.pop()


if __name__ == "__main__":
    print("Result of expression 2 1 + 3 * : " +
          str(evalRPN(["2", "1", "+", "3", "*"])))
    print("Result of expression 4 13 5 / + : " +
          str(evalRPN(["4", "13", "5", "/", "+"])))
    print("Result of expression 10 6 9 3 + -11 * / * 17 + 5 + : " +
          str(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])))
