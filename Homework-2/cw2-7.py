#cw 2.7

#1
D1 = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100,
     'CD':400, 'D':500, 'CM':900, 'M':1000}

roman1 = str(input('Wybierz liczbę spośród (I, IV, V, IX, X, XL, L, XC, C, CD,\
D, CM, M): '))

print('Rzymska liczba {} to arabska liczba {}.'.format(roman1, D1[roman1]))

#2
roman_list = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D',
              'CM', 'M']
arabic_list = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

D2 = dict(zip(roman_list, arabic_list, strict = True))

roman2 = str(input('Wybierz liczbę spośród (I, IV, V, IX, X, XL, L, XC, C, CD,\
D, CM, M): '))

print('Rzymska liczba {} to arabska liczba {}.'.format(roman2, D2[roman2]))

#3
D3 = dict([('I', 1), ('IV', 4), ('V', 5), ('IX', 9), ('X', 10), ('XL', 40), \
          ('L', 50), ('XC', 90), ('C', 100), ('CD', 400), ('D', 500), \
          ('CM', 900), ('M', 1000)])

roman3 = str(input('Wybierz liczbę spośród (I, IV, V, IX, X, XL, L, XC, C, CD,\
D, CM, M): '))

print('Rzymska liczba {} to arabska liczba {}.'.format(roman3, D3[roman3]))
