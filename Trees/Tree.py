#!/usr/bin/env python3


import abc
from collections.abc import Iterable, Container

class Tree(abc.ABC,Iterable):
    @abc.abstractmethod
    def root(self):
        pass

    @abc.abstractmethod
    def level(self, v):
        pass

    @abc.abstractmethod
    def height(self):
        pass

    @abc.abstractmethod
    def __len__(self):
        pass

    @abc.abstractmethod
    def leaves(self):
        pass

    @abc.abstractmethod
    def arity(self):
        pass

class TreeNode(abc.ABC, Container):
    @abc.abstractmethod
    def parent(self, v):
        pass

    @abc.abstractmethod
    def children(self, v):
        pass

    @abc.abstractmethod
    def isLeaf(self, v):
        pass

    @abc.abstractmethod
    def isRoot(self, v):
        pass

