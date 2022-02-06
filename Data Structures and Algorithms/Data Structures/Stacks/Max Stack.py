# Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.
# Grokking
# Leetcode https://leetcode.com/problems/max-stack/
# Solution https://leetcode.com/problems/max-stack/solution/
# Time Complexity Since this algorithm only traverses over the list once, it’s in linear time, O(n).
# Space Complexity The space complexity is O(n) because we store all elements in our map.


class MaxStack:

    def __init__(self):
        self.max_stack = []
        self.main_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)
        if not self.max_stack or x > self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])
        # print("->Push", x, self.main_stack, self.max_stack)

    def pop(self) -> int:
        # print("->Pop", self.main_stack, self.max_stack)
        if self.max_stack:
            self.max_stack.pop()
            return self.main_stack.pop()
        return None

    def top(self) -> int:
        # print("->Top", self.main_stack, self.max_stack)
        if self.main_stack:
            return self.main_stack[-1]
        return None

    def peekMax(self) -> int:
        # print("->PeekMax", self.main_stack, self.max_stack)
        if self.max_stack:
            return self.max_stack[-1]
        return None

    def popMax(self) -> int:
        # print("->PopMax", self.main_stack, self.max_stack)
        if self.max_stack:
            max_ele = self.peekMax()
            temp = []
            # print(max_ele)
            while self.top() != max_ele:
                temp.append(self.pop())
            # remove the element
            self.pop()
            # push back elements in reversed order to maintain state
            for ele in reversed(temp):
                self.push(ele)
            return max_ele
        return None


if __name__ == "__main__":
    stack = MaxStack()
    stack.push(5)
    stack.push(0)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(0)
    print("Main stack:", stack.main_stack)
    print("Max stack:", stack.max_stack)
    print("Maximum value: " + str(stack.peekMax()))
    stack.pop()
    stack.push(-2)
    print("Main stack:", stack.main_stack)
    print("Max stack:", stack.max_stack)
    print("Maximum value: " + str(stack.peekMax()))
    stack.pop()
    print("Main stack:", stack.main_stack)
    print("Max stack:", stack.max_stack)
    print("Maximum value: " + str(stack.peekMax()))
