#cw 8-2
##(a) Create an arbitrary one dimensional array called v1.
##(b) Create a new array v2 which consists of the odd indices of v1.
##(c) Create a new array v3 in backwards ordering from v1.

import numpy as np

v1 = np.arange(-4, 5, 0.75)
v2 = v1[::2].copy() # copy() is to make a separate array
v3 = v1[::-1].copy()

print('v1: ', v1)
print('v2: ', v2)
print('v3: ', v3)

input('Naciśnij klawisz: ')
#EOF
