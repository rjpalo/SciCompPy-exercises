#cw 9-1
#Plot functions sin(x), cos(x), and exp(-x) in a range [0,10] in the same
#figure. Colors are red, green, and blue, respectively. Lines are solid,
#dashed, and dotted, respectively. Add a legend.

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
a = np.sin(x)
b = np.cos(x)
c = np.exp(-x)

plt.plot(x, a, color = 'red', linestyle = 'solid', label = 'sin(x)')
plt.plot(x, b, color = 'green', linestyle = 'dashed', label = 'cos(x)')
plt.plot(x, c, color = 'blue', linestyle = 'dotted', label = 'exp(-x)')
plt.legend()
plt.show()

input('Naciśnij klawisz: ')
#EOF

