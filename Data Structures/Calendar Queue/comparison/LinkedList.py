from OrderedList import OrderedList
from ListNode import ListNode

class SinglyLinkedList(OrderedList):
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, prio, element):
        current_node = self.head
        previous_node = None
        node = ListNode(prio, element)

        while current_node is not None and node.prio > current_node.prio:
            previous_node = current_node
            current_node = current_node.next

        if previous_node is None:
            self.head = node
        else:
            previous_node.next = node

        node.next = current_node

    def getFirst(self):
        first = self.head
        if self.head is not None:
            self.head = self.head.next
        return first
    
    def peekFirst(self):
        return self.head

    def __len__(self):
        return self.size

    def __contains__(self, el):
        curr = self.head
        while curr != None:
            if curr is el: return True
            curr = curr.next
        return False
