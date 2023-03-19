#cw 3.2 - while loop

x = 1

while x < 41: 
    if x == 13:
        x += 1
        continue
    if x%5 == 0 and x%7 == 0:
        print('{} is divided by 5 and 7'.format(x))
        x +=1
    if x%7 == 0: 
        print('{} is divided by 7'.format(x))
        x += 1
    if x%5 == 0:
        print('{} is divided by 5'.format(x))
        x += 1
    else:
        print('{} is not important'.format(x))
        x += 1 


#eof
