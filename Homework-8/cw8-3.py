#cw 8-3
##(a) Create a two dimensional array called m1, shape=(4,5).
##(b) Create a new array m2 from m1, in which the elements of each row are
##in reverse order.
##(c) Create a new array m3 from m1, in which the elements of each column are
##in reverse order.
##(d) Cut off the first and last row and the first and last column of m1.

import numpy as np

m1 = np.random.randint(0, 100, size = (4, 5))
m2 = m1[:, ::-1].copy()
m3 = m1[::-1, :].copy()
m4 = m1[1:3, 1:4] 

print('m1:\n', m1)
print('m2:\n', m2)
print('m3:\n', m3)
print('m4:\n', m4)

input('Naciśnij klawisz: ')
#EOF
