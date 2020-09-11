class CircularQueue:

    def __init__(self,size):
        self.queue= [None] * size
        self.size=size
        self.read=0
        self.write=0

    # Adding elements to the queue
    def enqueue(self,data):
        if (self.write + 1) % self.size == self.read:   # CODA PIENA!
            return False
        self.queue[self.write]=data
        self.write = (self.write + 1) % self.size
        return True

    # Removing elements from the queue
    def dequeue(self):
        if self.read==self.write:   # CODA VUOTA!
            return None
        ret=self.queue[self.read]
        self.queue[self.read]=None
        self.read = (self.read + 1) % self.size
        return ret


####### TEST ######

'''q = CircularQueue(5)
print(q.enqueue(1))
print(q.enqueue(2))
print(q.enqueue(3))
print(q.enqueue(4))
print(q.enqueue(5))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())'''
