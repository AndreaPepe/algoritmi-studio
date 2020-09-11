from Tree import Tree,TreeNode
import random

class nTree(Tree):

    # defining Node methods and properties
    class _Node(TreeNode):

        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.parent=None
            self.children=[]

        def __repr__(self):
            return str(self)

        def __str__(self):
            return str(self.key) + ": " + str(self.value)

        def __contains__(self,key):
            return self.key==key

        def getChild(self,i):
            if i>=len(self.children):
                return None
            return self.children[i]

        def addChild(self,key,value):
            child = nTree._Node(key,value)
            child.parent=self
            self.children.append(child)

        def removeChild(self,key):
            for child in self.children:
                if child.key==key:
                    self.children.remove(child)
                    return True
            return False

        def parent(self):
            return self.parent

        def children(self):
            return self.children

        def isLeaf(self):
            return len(self.children)==0

        def isRoot(self):
            return self.parent == None

    ###################################################################

    #defining methods of the nTree:

    def __init__(self,rootKey,rootVal):
        self.root=nTree._Node(rootKey,rootVal)

    def root(self):
        return self.root

    def level(self,v):
        l=0
        while v!=self.root:
            l += 1
            v=v.parent
        return l

    def height(self):
        return self.level(max(self.leaves(), key=lambda x: self.level(x)))

    def __len__(self):
        return sum(1 for _ in iter(self))

    def leaves(self):
        leaves=[]
        for node in self:
            if node.isLeaf():
                leaves.append(node)
        return leaves

    def arity(self):
        arity=0
        for node in self:
            arity=max(arity,len(node.children))
        return arity

    def getRandomNode(self):
        num = int(len(self) * random.random())
        count = 0
        for node in self:
            if num==count:
                return node
            count +=1

    def __iter__(self):
        # This is a BFS search
        queue=[]
        queue.append(self.root)

        while(len(queue) > 0):
            yield queue[0]
            node = queue.pop(0)
            queue.extend(node.children)

    def __str__(self):
        return self._getStrLevel(self.root,0)

    def _getStrLevel(self,v,level):
        ret=""
        if v:
            if v == self.root:
                ret += str(v.key) + "\n"
            else:
                ret += "|  " *(level-1) + "\_" + str(v.key) + "\n"
            for child in v.children:
                ret += self._getStrLevel(child,level+1)
        return ret
