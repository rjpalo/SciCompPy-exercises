#cw 4-3

#(a) iter_even - produce even numbers

def iter_even():
    '''produce even numbers >= 0'''
    a = 0
    yield a
    while True:
        a += 2
        yield a

#check
parzyste = iter_even()
for i in parzyste:
    print(i)
    if i > 30:
        break

print('----------') # dla wizualnego oddzielenia
#(b) iter_odd - produce odd numbers

def iter_odd():
    '''produce odd numbers >= 1'''
    b = 1
    yield b
    while True:
        b += 2
        yield b

#check
nieparzyste = iter_odd()
for i in nieparzyste:
    print(i)
    if i > 30:
        break

print('----------')
#(c) iter_power(k) - produce powers of k

def iter_power(k):
    '''produce powers of k'''
    c = 0
    d = k**0
    e = k
    yield c
    yield d
    yield e
    while True:
        e = e*k
        yield e

#check
k = int(input('Wpisz liczbę, którą chcesz spotęgować: '))
potegi = iter_power(k)
for i in potegi:
    if k == 0 or k == 1:
        print(0)
        print(1)
        print(f"it's {k} all the way down")
        break
    else:
        print(i)
        if i > 30:
            break

#eof
