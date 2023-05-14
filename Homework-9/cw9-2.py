#cw 9-2
#Generate n=100 random points in a unit square [0,1]x[0,1]. Points are green
#if the distance from (0,0) is less then 1; they are red otherwise. The marker
#area of a point (x,y) should be proportional to |x|+|y|.

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4)
x = np.random.rand(100)
y = np.random.rand(100)
hue = np.where(x**2 + y**2 < 1, 'g', 'r')
area = 75*(abs(x) + abs(y))

plt.scatter(x, y, s = area, c = hue, alpha = 0.5)
plt.show()

input('Naciśnij klawisz: ')
#EOF
