#!/usr/bin/env python3

from CalQueue import CalQueue
import random
import string
import sys

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

cq = CalQueue()

tries = int(sys.argv[1])
lastmin = 0.0

for i in range(tries):
    prio = 1000 * random.random()
    print("Enqueueing at", "{:.9f}".format(prio),"\t","{:.2f}".format(i/tries*100),"%")
    cq.enqueue(prio, randomString())

for i in range(tries):
    curr = cq.getMin()
    assert(curr.prio >= lastmin)
    lastmin = curr.prio
    print("Dequeued",curr)
