class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __str__(self):
        curr = self
        output = ""
        while curr:
            output += str(curr.value)+" "
            curr = curr.next
        return output
# We usually don't initialize a linked list in this manner
# class LinkedList(object):
#     def __init__(self, node):
#         self.head = node

def list2LinkedList(nums):
    head = None
    curr = None
    for n in nums:
        if not head:
            curr = Node(n)
            head = curr
        else:
            curr.next = Node(n)
            curr = curr.next
    return head

head = Node(1, Node(2, Node(3)))
print(head)

print(list2LinkedList([10, 20, 30]))