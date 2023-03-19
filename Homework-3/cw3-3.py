#cw. 3-3

import math

n = 2022
x = math.pi
word = 'Python'
polish = 'książka'

with open('vars.txt', 'w', encoding = 'utf-8') as outfile:
    outfile.write('{0}\n{1:.5f}\n{2}\n{3}'.format(n, x, word, polish))

with open('vars.txt', 'r', encoding = 'utf-8') as infile:
    lines = infile.read() #bo mały plik
    print(lines)

#eof
