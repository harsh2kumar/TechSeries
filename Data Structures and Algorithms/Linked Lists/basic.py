class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

# We usually don't initialize a linked list in this manner
# class LinkedList(object):
#     def __init__(self, node):
#         self.head = node
