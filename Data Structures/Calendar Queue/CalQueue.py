import math
from PriorityQueue import PriorityQueue
from LinkedList import SinglyLinkedOrderedList

class CalQueue(PriorityQueue):
    def __init__(self):
        self.size = 0
        self.numOfBuckets = 2       # n
        self.bucketWidth = 1.0      # w
        self.bucketTop = 1.5
        self.lastPrio = 0
        self.lastBucket = 0

        self.bottomThreshold = self.numOfBuckets // 2 - 2
        self.topThreshold = 2 * self.numOfBuckets

        self.buckets = self._init_buckets(self.numOfBuckets)
        self.resizeEnabled = True

    def __len__(self):
        return self.size

    def __contains__(self, el): None

    def enqueue(self, prio, el):
        # Sanity check
        if prio < self.lastPrio and self.resizeEnabled:
            raise ValueError("You cannot insert an element in the past!")

        bucket = int(prio // self.bucketWidth) # Virtual bucket
        bucket = bucket % self.numOfBuckets # Physical bucket
        self.buckets[bucket].insert(prio, el)
        self.size += 1
        if self.size > self.topThreshold:
            self._resize(2 * self.numOfBuckets)

    def getMin(self):
        if self.size == 0:
            return None

        i = self.lastBucket
        while True:
            node = self.buckets[i].peekFirst()
            if node is not None and node.prio < self.bucketTop:
                # Dequeue the element
                node = self.buckets[i].getFirst()
                self.size -= 1

                # Update position on calendar
                self.lastBucket = i
                self.lastPrio = node.prio

                # Halve the calendar if needed
                if self.size < self.bottomThreshold:
                    self._resize(self.numOfBuckets // 2)

                # Return the element
                return node
            else:
                # Go to the next virtual bucket
                i = (i + 1) % self.numOfBuckets
                self.bucketTop += self.bucketWidth # Beware of accumulation of errors!

                # Did we scan the whole calendar once?
                if i == self.lastBucket:
                    break

        # Direct search for optimization purposes
        lowest = math.inf
        lowestBucket = 0
        for i in range(0, self.numOfBuckets):
            node = self.buckets[i].peekFirst()
            if node is not None and node.prio < lowest:
                lowest = node.prio
                lowestBucket = i

        # We know now where to find the minimum
        self.lastPrio = lowest
        self.bucketTop = (self.lastPrio // self.bucketWidth + 1) * self.bucketWidth + 0.5 * self.bucketWidth
        self.lastBucket = lowestBucket
        return self.getMin()

    def _resize(self, nbucks):
        if self.resizeEnabled == False:
            return

        # To prevent unwanted recursive calls to _resize
        self.resizeEnabled = False

        # Save the configuration of the current calendar
        old_nbucks = self.numOfBuckets
        old_buckets = self.buckets

        # Reconfigure the calendar
        newwidth = self._newWidth()
        self.bucketWidth = newwidth
        self.numOfBuckets = nbucks
        self.buckets = self._init_buckets(nbucks)
        self.bottomThreshold = self.numOfBuckets // 2 - 2
        self.topThreshold = 2 * self.numOfBuckets

        virtualBucket = int(self.lastPrio // self.bucketWidth)
        self.lastBucket = virtualBucket % self.numOfBuckets
        self.bucketTop = (virtualBucket + 1) * self.bucketWidth + 0.5 * self.bucketWidth

        # Copy the elements to the new calendar
        for i in range(old_nbucks):
            node = old_buckets[i].getFirst()
            while node is not None:
                self.enqueue(node.prio, node.data)
                node = old_buckets[i].getFirst()


        self.resizeEnabled = True

    def _newWidth(self):
        # Determine how many samples should be used to
        # recompute the new bucket width
        if self.size < 2:
            return 1.0
        if self.size <= 5:
            nsamples = self.size
        else:
            nsamples = 5 + self.size // 10
        if nsamples > 25:
            nsamples = 25

        # Store the current calendar configuration
        lastprio = self.lastPrio
        lastbucket = self.lastBucket
        buckettop = self.bucketTop

        # Keep track of artificially extracted nodes
        nodes = [None] * nsamples

        # Compute the average separation
        average = 0.0
        for i in range(nsamples):
            nodes[i] = self.getMin()
            if i > 0:
                average += nodes[i].prio - nodes[i - 1].prio;
        average /= nsamples - 1

        # Recalculate average ignoring large separations
        # Beware that these enqueues are breaking calqueue invariants!
        self.enqueue(nodes[0].prio, nodes[0].data)
        newaverage = 0.0
        count = 0
        for i in range(1, nsamples):
            if nodes[i].prio - nodes[i - 1].prio < average * 2:
                count += 1
                newaverage += nodes[i].prio - nodes[i - 1].prio

            self.enqueue(nodes[i].prio, nodes[i].data)

        # Compute the new width
        new_width = newaverage / count * 3.0

        # Restore the configuration of the calendar
        self.lastPrio = lastprio
        self.lastBucket = lastbucket
        self.bucketTop = buckettop

        return new_width

    def _init_buckets(self, size):
        buckets = [None] * size
        for i in range(size):
            buckets[i] = SinglyLinkedOrderedList()
        return buckets
