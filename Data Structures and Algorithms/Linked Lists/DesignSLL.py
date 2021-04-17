# Design a Linked List
# Refer to https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
# Solution https://leetcode.com/problems/design-linked-list/solution/

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):
    """
    TIME COMPLEXITY:
    get, addAtIndex, deleteAtIndex - O(K) where K is the value of index
    addAtHead - O(1)
    addAtTail - O(N), where N is the size of the list

    SPACE COMPLEXITY:
    O(1) for all operations
    """

    def __init__(self):
        """
        Initialize your data structure here.
        Note, that sentinel node is used as a pseudo-head and is always present. This way the structure could never be empty, it will contain at least a sentinel head. 
        All nodes in MyLinkedList have a type ListNode: value + link to the next element.
        """
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # invalid index
        # 0th index is the sentinel node, hence, it needs to be counted as invalid
        # if size of LL is 0 and user asks for 0th node, return invalid
        # SLL is 0-indexed i.e. first node should start from 0, hence max_possible_index<self.size
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        # iterate for index + 1 steps due to addition of sentinel node
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, 
        the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # return if index>size of LL
        if index > self.size:
            return
        # if index is negative insert at the beginning of the LL
        if index < 0:
            index = 0
        pred_node = self.head
        # find the pred node of the index where the new node is to be added
        for _ in range(index):
            pred_node = pred_node.next
        # insert the new node
        to_add = ListNode(val)
        to_add.next = pred_node.next
        pred_node.next = to_add
        # increase size of LL
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # return if index>size of LL
        # SLL is 0-indexed i.e. first node should start from 0, hence max_possible_index<self.size
        if index < 0 or index >= self.size:
            return
        pred_node = self.head
        # find the pred of node to be deleted
        for _ in range(index):
            pred_node = pred_node.next
        # deleting pred's next node
        pred_node.next = pred_node.next.next
        # increase size of LL
        self.size -= 1
