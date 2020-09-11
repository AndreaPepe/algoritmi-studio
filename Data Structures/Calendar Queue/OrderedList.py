import abc
from collections.abc import Container, Sized

class OrderedList(abc.ABC, Container, Sized):
    @abc.abstractmethod
    def insert(self, prio, element):
        pass

    @abc.abstractmethod
    def getFirst(self):
        pass

    @abc.abstractmethod
    def peekFirst(self):
        pass

