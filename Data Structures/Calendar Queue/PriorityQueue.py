import abc
from collections.abc import Container, Sized

class PriorityQueue(abc.ABC, Container, Sized):
    @abc.abstractmethod
    def enqueue(self, prio, el):
        pass

    @abc.abstractmethod
    def getMin(self):
        pass

