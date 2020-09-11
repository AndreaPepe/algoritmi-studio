from collections.abc import MutableSet

class CircularList(MutableSet):

    class _Node():
        def __init__(self,data):
            self.data=data
            self.prev=None
            self.next=None
            self.list=None

        def __next__(self):
            node=self.next
            if node == self.list.head:  # skip sentinel and go ahead to the next
                node=node.next
            return node

        def __str__(self):
            return str(self.data)

    ######################################################################


    def __init__(self):
        self.head=self._getNode(None)
        self.head.next=self.head    # at the beginning the sentinel points itself
        self.head.prev=self.head
        self.size=0

    def _getNode(self,element):
        node=CircularList._Node(element)
        node.list=self
        return node

    def add(self,element):
        return self.addAfter(element,self.head)

    def addAfter(self,element,predecessor):
        node=self._getNode(element)
        node.next=predecessor.next
        node.prev=predecessor
        predecessor.next.prev=node
        predecessor.next=node
        self.size+=1
        return node

    def discard(self,element):
        for node in self:
            if node.data==element:
                node.prev.next=node.next
                node.next.prev=node.prev
                node.next=None
                node.prev=None
                self.size-=1
                return

    def __contains__(self,element):
        hasIt=False
        for node in self:
            if node.data==element:
                hasIt=True
        return hasIt

    def __len__(self):
        return self.size

    def __iter__(self):
        current=self.head
        return self

    def __next__(self,current):
        node=current.next
        if node == self.head:
            raise StopIteration
        return self.head

    def __str__(self):
        dump="["
        for node in self:
            dump += str(node) + ","
        dump += "]"
        return dump
