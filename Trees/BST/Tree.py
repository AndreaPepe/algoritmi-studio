#!/usr/bin/env python3
import sys
import abc
from abc import abstractmethod

if sys.version_info[0] == 3:
    from abc import ABC
    from collections.abc import Iterable, Container
    myABC = ABC
else:
    from abc import ABCMeta
    from collections import Iterable, Container
    myABC = ABCMeta

# this get __iter__ from Iterable
class Tree(Iterable):
    __metaclass__ = myABC
    @abstractmethod
    def root(self):
        pass
    @abstractmethod
    def level(self, v):
        pass
    @abstractmethod
    def height(self):
        pass
    @abstractmethod
    def __len__(self):
        pass
    @abstractmethod
    def leaves(self):
        pass
    @abstractmethod
    def arity(self):
        pass
# this get __contains__ from Container
class TreeNode(Container):
    __metaclass__ = myABC
    
    @abstractmethod
    def parent(self, v):
        pass

    @abstractmethod
    def leftChild(self, v):
        pass

    @abstractmethod
    def rightChild(self, v):
        pass

    @abstractmethod
    def isLeaf(self, v):
        pass

    @abstractmethod
    def isRoot(self, v):
        pass
