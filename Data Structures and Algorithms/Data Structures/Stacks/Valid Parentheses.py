# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# Grokking
# Leetcode https://leetcode.com/problems/valid-parentheses/
# Solution https://leetcode.com/problems/valid-parentheses/solution/
# Time Complexity Since this algorithm only traverses over the string once, it’s in linear time, O(n).
# Space Complexity The space complexity is O(n) because we can store all characters in our stack.

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    # The stack to keep track of opening brackets.
    stack = []

    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for char in s:

        # If the character is an closing bracket
        if char in mapping:

            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            top_element = stack.pop() if stack else '#'

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack


if __name__ == "__main__":
    print("(): ", isValid("()"))
    print("()[]{}: ", isValid("()[]{}"))
    print("(]: ", isValid("(]"))
