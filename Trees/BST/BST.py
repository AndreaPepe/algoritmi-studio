from BinaryTree import BinaryNode,BinaryTree

class BSTNode(BinaryNode):
    pass

class BinarySearchTree(BinaryTree):

    def __init__(self):
        self.root=None

    def insert(self,key,data):
        new = BSTNode(key,data)
        self.internal_insert(new)
        return new

    def internal_insert(self,new):
        parent=None
        current=self.root

        while current is not None:
            parent=current
        # using the FUNDAMENTAL PROPERTY of Binary Search Trees
            if new.key <= current.key:
                current = current.left
            else:
                current = current.right

        new.parent=parent                   # attacking child to parent

        # child is root, left child or right child?
        if parent is None:
            self.root = new
        elif new.key <= parent.key:
            parent.left = new
        else:
            parent.right = new
        return new

    def delete(self,key):
        z=self.search(key)      # nodo da eliminare

        if z.left is None or z.right is None:       # caso in cui ha 0 (radice) o 1 solo figlio
            y=z
        else:
            y=self.successor(z)

        if y.left is not None:
            x=y.left
        else:
            x=y.right

        if x is not None:
            x.parent=y.parent

        # sgancio y
        if y.parent is None:
            self.root = x
        elif y==y.parent.left:
            y.parent.left=x
        else:
            y.parent.right=x

        if y!=z:
            z.key=y.key
        return y

    def search(self,key):
        current = self.root
        while current is not None and current.key!=key:
            if key <= current.key:
                current=current.left
            else:
                current=current.right
        return current

    def successor(self,v):
        if v.right is not None:
            return self.minimum(v.right)
        y=v.parent
        while y is not None and x==y.right:
            x=y
            y=y.parent
        return y

    def minimum(self,v):
        while v is not None and v.left is not None:
            v=v.left
        return v

    def maximum(self,v):
        while v is not None and v.right is not None:
            v=v.right
        return v
