#cw 3.2 - for loop

S = ''

for x in range(1, 41):
    if x == 13:
        continue
    elif x%5 == 0 and x%7 == 0:
        S = 'is divided by 5 and 7'
    elif x%5 == 0:
        S = 'is divided by 5'
    elif x%7 == 0:
        S = 'is divided by 7'
    else:
        S = 'is not important'
    print(x, S)


#eof
