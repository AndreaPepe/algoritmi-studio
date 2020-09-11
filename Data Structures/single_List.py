from collections.abc import Container
from collections.abc import MutableSequence

class ListNode(Container):

    def __init__(self,data):
        self._data=data
        self.next=None      # unico puntatore al successivo nodo

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self,value):
        self._data=value

    def __contains__(self,item):
        return (self.data==item)

    def __str__(self):
        return str(self.data)

################################################################################



class SinglyLinkedList(MutableSequence):

    def __init__(self):
        self.head = None
        self.tail = None   # puntatori a testa e coda per inserimenti in O(1)

    def insert(self,index,element):
        count = 0
        current=self.head
        prev = None
        new_node = ListNode(element)    # new node

        while current is not None and count<index:
            prev=current
            current=current.next
            count+=1

        if count < index-1:
            raise IndexError("Index " + str(index) + " does not fit in list!\n")

        if prev is None:    # inserimento IN TESTA
            self.head = new_node
        else:
            prev.next = new_node

        if current is None: # inserimento in CODA
            self.tail.next = new_node
            self.tail =new_node
        else:
            new_node.next=current



    def append(self,element):
        node = ListNode(element)
        if self.head == None:   #lista vuota
            self.head=node
        else:
            self.tail.next=node
        self.tail=node

    def appendLeft(self,element):
        node = ListNode(element)
        if self.tail == None:
            self.tail = node
        node.next=self.head
        self.head=node

    def _getitem(self, index):
        count = 0
        current_node = self.head
        while current_node is not None and count < index:
            current_node = current_node.next
            count += 1

        if current_node is None and count != index:
            return None
        return current_node

    def __getitem__(self, index):
        node = self._getitem(index)
        if node is None:
            print('No element at index', index)
            raise IndexError('No element at index', index)
        return self._getitem(index).data

    def __setitem__(self, index, value):
        node = self._getitem(index)
        node.data = value

    def __delitem__(self, index):
        if index == 0:
            self.head = self.head.next
            return

        previous = self._getitem(index - 1)
        if previous is None:
            return

        if previous.next == self.tail:
            self.tail = previous
            self.tail.next = None
            return

        previous.next = previous.next.next


    def __len__(self):
            count = 0
            current_node = self.head

            while current_node is not None:
                count = count + 1
                current_node = current_node.next

            return count

    def __str__(self):
            current_node = self.head
            dump = "["

            while current_node is not None:
                dump += str(current_node) + ","
                current_node = current_node.next

            dump += "]"
            return dump
