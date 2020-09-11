from collections.abc import Container
from collections.abc import MutableSequence

class ListNode(Container):

    def __init__(self,data):
        self._data=data
        self.next=None
        self.prev=None      # puntatore anche al PRECEDENTE!!!

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __contains__(self, value):
        if self.data == value:
            return True
        else:
            return False

    def __str__(self):
        return str(self.data)

################################################################################


class DoublyLinkedList(MutableSequence):
    def __init__(self):
        self.head = ListNode(None)      # NODI SENTINELLA
        self.tail = ListNode(None)
        self.head.next = self.tail      #default
        self.tail.prev = self.head
        self.size = 0

    def insert_between(self,node,predecessor,successor):
        node.next=successor
        node.prev=predecessor
        predecessor.next=node
        successor.prev=node
        self.size+=1

    def insert(self,index,element):
        node=ListNode(element)
        successor=self._getitem(index)
        predecessor=successor.prev
        self.insert_between(node,predecessor,successor)

    def append(self,element):
        node = ListNode(element)
        successor=self.tail
        predecessor=successor.prev
        self.insert_between(node,predecessor,successor)

    def appendLeft(self,element):
        node=ListNode(element)
        predecessor=self.head
        successor=predecessor.next
        self.insert_between(node,predecessor,successor)

    def __reversed__(self):
        # print the list from tail to head
        current=self.tail.prev
        while current is not self.head:
            yield current.data
            current=current.prev

    def _getitem(self,index):
        count=0
        current=self.head.next
        while current in not self.tail and count<index:
            current=current.next
            count+=1

        if current is None and count!=index:
            return None
        return current

    def __getitem__(self,index):
        node=self._getitem(index)
        if node is None:
            print("No item at index ",index)
            raise IndexError("No item at index ",index)
        return self._getitem(index).data

    def __setitem__(self,index,value):
        node=self._getitem(index)
        node.data=value

    def __delitem__(self,index):
        node=self._getitem(index)
        predecessor=node.prev
        successor=node.next
        predecessor.next=successor
        successor.prev=predecessor
        node.next=node.prev=None    # STACCARE IL NODO
        self.size -= 1
        return node.data

    def __len__(self):
        return self.size

    def __str__(self):
        current=self.head.next
        dump="["

        while current is not self.tail:
            dump += str(current) + ","
            current=current.next

        dump += "]"
        return dump

        
