#!/usr/bin/env python3

from nTree import nTree
import random
import string

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


T = nTree(1, "rootNode")

for i in range(80):
    node = T.getRandomNode()
    node.addChild(int(100 * random.random()), randomString())

print(T._getStrLevel(T.root,0))

print("Total nodes:", len(T))
print("Tree height:", T.height())
print("Leaves:", len(T.leaves()))
print("Arity:", T.arity())
