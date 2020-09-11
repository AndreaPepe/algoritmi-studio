import ctypes
from collections.abc import Collection

class dynamicArray (Collection):

    def __init__(self):
        self.n = 0    #default number of elements
        self.capacity = 1 #default capacity of Array
        self.A = self._make_array(self.capacity)
        self.count = 0

    def __len__(self):
        return (self.n)  # alternatively: return len(self.A)

    def __contains__(self,item):
        return item in self.A

    def __iter__(self):
        self.count=0
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        else:
            self.count += 1
            return self[self.count -1]

    def __getitem__(self,k):
        if not 0 <= k < self.n:
            raise IndexError("Index " + str(k) + " is out of bounds!\n")
        return self.A[k]

    def append(self,elem):
        if self.n == self.capacity:     # resize the array!!!
            self._resize(2 * self.capacity)

        self.A[self.n] = elem
        self.n += 1

    def _resize(self,new_cap):
        B=self._make_array(new_cap)

        for k in range(self.n):     # copy of the already inserted elements
            B[k]=self.A[k]

        self.A=B
        self.capacity=new_cap

    def _make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()
