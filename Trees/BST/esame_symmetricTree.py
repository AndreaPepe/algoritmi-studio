from BST import BinarySearchTree
class BinaryTree:

 class Node:
  def __init__(self,val):
   self.val=val
   self.left=None
   self.right=None

 def __init__(self):
  self.root=None


def isSymmetric(T):
 root = T.root
 return isSpecular(root.left,root.right)

def isSpecular(l,r):
 if l == None and r == None:
  return True
 elif l != None and r != None:
  if isSpecular(l.left,r.right) and isSpecular(l.right,r.left):
   return True
  else:
   return False
 else:
  return False


T=BinarySearchTree()
T.insert(5,0)
T.insert(3,0)
T.insert(1,0)
T.insert(6,0)
T.insert(9,0)
T.insert(8,0)

print(isSymmetric(T))
