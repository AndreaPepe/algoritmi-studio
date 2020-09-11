class MaxMinPrio:

    class Node:
        def __init__(self,val):
            self.val=val
            self.left=None
            self.right=None

    def __init__(self):
        self.root=None
        self.min=None
        self.max=None

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max

    def insert(self,val):
        leftMost=rightMost=True         # sentinelle per aggiornare max e min
        newNode=MaxMinPrio.Node(val)

        x=self.root
        y=None
        while x!=None:
            y=x
            if val<x.val:
                rightMost=False
                x=x.left
            else:
                leftMost=False
                x=x.right

        if y==None:
            self.root=newNode
        elif val<y.val:
            rightMost=False
            y.left=newNode
        else:
            leftMost=False
            y.right=newNode
