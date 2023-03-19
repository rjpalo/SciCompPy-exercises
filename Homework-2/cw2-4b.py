#cw. 2.4b

numbers = [x for x in range(1,11)]
names = ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon',
         'Nitrogen', 'Oxygen', 'Fluorine', 'Neon']
symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
masses = [1, 4, 6.94, 9, 10.81, 12, 14, 16, 19, 20.18]

line_sep = ['-'.ljust(3, '-'), '-'.ljust(20, '-'), '-'.ljust(6, '-'),
                  '-'.ljust(10, '-')]
header = ['No.'.center(3), 'Name (en)'.ljust(20), 'Symbol'.center(6),
          'Weight (u)'.center(10)]

pt = list(zip(numbers, names, symbols, masses, strict = True))

print('+' + '+'.join(line_sep) + '+') #rancik górny
print('|' + '|'.join(header) + '|') #nagłówek
print('+' + '+'.join(line_sep) + '+') #rancik środkowy

for element in pt:
    a = str(element[0]).rjust(3)
    b = str(element[1]).ljust(20)
    c = str(element[2]).center(6)
    d = str(element[3]).rjust(10)   

    print('|', end = '')
    print(a, b, c, d, sep = "|", end = '|\n')

print('+' + '+'.join(line_sep) + '+') #rancik dolny

