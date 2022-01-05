# Implement the function reverseK(queue, k) which takes a queue and a number “k” as input and reverses the first “k” elements of the queue.
# Grokking https://www.educative.io/module/lesson/data-structures-in-python/B8E195GVv4Y
# Leetcode
# Solution
# Time Complexity Since this algorithm only traverses over the list twice, it’s in linear time, O(n).
# Space Complexity The space complexity is O(k).


from Queue import MyQueue
from Stack import MyStack

# 1.Push first k elements in queue in a stack.
# 2.Pop Stack elements and enqueue them at the end of queue
# 3.Dequeue queue elements till "k" and append them at the end of queue


def reverseK(queue, k):
    # Handling invalid input
    if k < 0 or queue.is_empty() or k > queue.size():
        return None
    # dequeue first k elements and push them to stack
    stack = MyStack()
    for _ in range(k):
        stack.push(queue.dequeue())
    # pop k elements from stack and enqueue them in queue
    # this will add k elements in reversed order to queue
    while not stack.is_empty():
        queue.enqueue(stack.pop())
    # dequeue n-k elements and add them to the queue
    n = queue.size()
    for _ in range(n-k):
        queue.enqueue(queue.dequeue())
    return queue


if __name__ == "__main__":
    # testing our logic
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)
    queue.enqueue(7)
    queue.enqueue(8)
    queue.enqueue(9)
    queue.enqueue(10)
    print("the queue before reversing:")
    print(queue.items)
    reverseK(queue, 5)
    print("the queue after reversing:")
    print(queue.items)
