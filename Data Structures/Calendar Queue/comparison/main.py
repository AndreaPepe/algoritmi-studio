#!/usr/bin/env python3

from LinkedList import SinglyLinkedList
import random
import string
import sys

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

ll = SinglyLinkedList()

tries = int(sys.argv[1])
lastmin = 0.0

for i in range(tries):
    prio = 1 * random.random()
    print("Enqueueing at", "{:.9f}".format(prio),"\t","{:.2f}".format(i/tries*100),"%")
    ll.insert(prio, randomString())

for i in range(tries):
    curr = ll.getFirst()
    assert(curr.prio >= lastmin)
    lastmin = curr.prio
    print("Dequeued",curr)
