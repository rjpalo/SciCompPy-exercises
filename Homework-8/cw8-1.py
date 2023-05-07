#cw 8-1
#Create the following NumPy arrays:
#(a) float from 0.0 to 1.0 step 0.1, shape=(11,)
#(b) int zeros (1 byte) with shape=(5,6)
#(c) complex with shape=(9,), powers of x = complex(0, 1): 1, x, x**2, ...,
# x**8.

import numpy as np

a1 = np.linspace(0.0, 1.0, num = 11)
a2 = np.arange(0.0, 1.1, 0.1)
b = np.zeros((5, 6), dtype = int)

x = complex(0, 1)
c = np.array([x**n for n in range(9)], dtype = complex)

print('a(1): ', a1)
print('a(2): ', a2)
print('b:\n', b)
print('c: ', c)

input('Naciśnij klawisz: ')
#EOF
