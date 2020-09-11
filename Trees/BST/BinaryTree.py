#!/usr/bin/env python3

from Tree import Tree, TreeNode
import random

class BinaryNode(TreeNode):
    def __init__(self, key, data):
        self.key = key          # key associated to the payload
        self.data = data        # the actual payload of the node
        self.parent = None      # keeps track of the parent (only a root node can have this equal to None)
        self.left = None        # keeps track of the left (right) child (only a leaf has both equal to None)
        self.right = None       #
        
    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.key) + ": " + str(self.data)

    def __contains__(self, key):
        return self.key == key

    def parent(self):
        return self.parent

    def leftChild(self):
        return self.left

    def rightChild(self):
        return self.right

    def isLeaf(self):
        return self.left == None and self.right == None

    def isRoot(self):
        return self.parent == None

    def height(self):
        lh = 0
        rh = 0
        if self.left:  lh = self.left.height() 
        if self.right: rh = self.right.height() 
        return 1 + max(lh, rh) 

    def children(self):
        res = []
        if self.left:
            res.append(self.left) 
        if self.right:
            res.append(self.right) 
        return res

class BinaryTree(Tree):
    def __init__(self):
        self.root = None

    def root(self):
        return self.root

    #takes a node and returns its level 
    def level(self, v):                                         # get the current level of the node passed as parameter!
        l = 0
        while v != self.root:
            l += 1
            v = v.parent
        return l

    def height(self):
        return self.root.height()

    def __len__(self):
        return sum(1 for _ in iter(self))

    def leaves(self):
        leaves = []
        for node in self:
            if node.isLeaf():
                leaves.append(node)
        return leaves

    def arity(self):
        arity = 0
        for node in self:
            arity = max(arity, len(node.children()))
        return arity

    def __iter__(self):
        # Implementa una BFS
        queue = [] 
        queue.append(self.root)
  
        while(len(queue) > 0): 
            yield queue[0] 
            node = queue.pop(0) 
            queue.extend(node.children()) 

    def __str__(self):
        ret = ""
        lines, _, _, _ = BinaryTree._display(self.root)
        for line in lines:
            ret += line + "\n"
        return ret

    @staticmethod
    def _display(node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = BinaryTree._display(node.left)
            s = '%s' % node.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = BinaryTree._display(node.right)
            s = '%s' % node.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = BinaryTree._display(node.left)
        right, m, q, y = BinaryTree._display(node.right)
        s = '%s' % node.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
