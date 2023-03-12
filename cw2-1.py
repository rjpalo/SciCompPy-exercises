#cw 2.1

import random

N = random.randint(pow(10,6),pow(10,20))
Nswitch = str(N)

zero_counter = 0

for char in Nswitch:
    if char == "0":
        zero_counter += 1

print(f'Liczba {N} ma {zero_counter} zer(a).')

