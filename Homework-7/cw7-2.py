#cw 7-2
##Create the following infinite iterators:

import itertools
import random

class RandoInt:

    def __init__(self):
        self.n = 0

    def __call__(self):
        self.n = random.choice([0, 1])
        return self.n


#returning 0, 1, 0, 1, 0, 1, ...,

it1 = itertools.cycle([0, 1])

print('check it1')
for i in range(20):
    print(next(it1), end = ' ')

#returning randomly 0 or 1 on demand

it2 = iter(RandoInt(), 2)

print('\ncheck it2')
for i in range(20):
    print(next(it2), end = ' ')

#returning 0, 1, 0, -1, 0, 1, 0, -1, ...

it3 = itertools.cycle([0, 1, 0, -1])

print('\ncheck it3')
for i in range(20):
    print(next(it3), end = ' ')
