# You have to implement the enqueue() and dequeue() functions using the MyStack class we created earlier. enqueue() will insert a value into the queue and
# dequeue() will remove a value from the queue.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/NEGmmvoVEEz
# Leetcode https://leetcode.com/problems/implement-queue-using-stacks/
# Solution https://leetcode.com/problems/implement-queue-using-stacks/solution/
# Two Stacks Working in enqueue()
# enqueue is O(n); dequeue is O(1)
# Two Stacks Working in dequeue()
# enqueue is O(1); dequeue is O(n)

# We can use 2 stacks for this purpose,main_stack to store original values
# and temp_stack which will help in enqueue operation.
# Main thing is to put first entered element at the top of main_stack

from Stack import MyStack
# We can use 2 stacks for this purpose,main_stack to store original values
# and temp_stack which will help in enqueue operation.
# Main thing is to put first entered element at the top of main_stack

from Stack import MyStack


class TwoStackEnqueue:
    # Can use size from argument to create stack
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

    # Inserts Element in the Queue
    def enqueue(self, value):
        # Push the value into main_stack in O(1)
        if self.main_stack.is_empty() and self.temp_stack.is_empty():
            self.main_stack.push(value)
            print(str(value) + " enqueued")
        else:
            while not self.main_stack.is_empty():
                self.temp_stack.push(self.main_stack.pop())
            # inserting the value in the queue
            self.main_stack.push(value)
            print(str(value) + " enqueued")
            while not self.temp_stack.is_empty():
                self.main_stack.push(self.temp_stack.pop())

    # Removes Element From Queue
    def dequeue(self):
        # If stack empty then return None
        if self.main_stack.is_empty():
            return None
        value = self.main_stack.pop()
        print(str(value) + " dequeued")
        return value


class TwoStackDequeue:

    # Can use size from argument to create stack
    def __init__(self):
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

        # Inserts Element in the Queue
    def enqueue(self, value):
        # Push the value into main_stack in O(1)
        self.main_stack.push(value)
        print(str(value) + " enqueued")

        # Removes Element From Queue
    def dequeue(self):
        # If both stacks are empty, end operation
        if not self.temp_stack.is_empty():
            front = self.temp_stack.pop()
            print(str(front) + " dequeued")
            return front
        if self.temp_stack.is_empty() and self.main_stack.is_empty():
            return None
          # Transfer all elements to temp_stack
        while not self.main_stack.is_empty():
            self.temp_stack.push(self.main_stack.pop())
        # Pop the first value. This is the oldest element in the queue
        front = self.temp_stack.pop()
        print(str(front) + " dequeued")
        return front


if __name__ == "__main__":
    print("Two Stacks working in enqueue()")
    queue = TwoStackEnqueue()
    for i in range(5):
        queue.enqueue(i+1)
    print("----------")
    for i in range(5):
        queue.dequeue()

    print("\nTwo Stacks working in dequeue()")
    queue = TwoStackDequeue()
    for i in range(5):
        queue.enqueue(i+1)
    print("----------")
    for i in range(5):
        queue.dequeue()
