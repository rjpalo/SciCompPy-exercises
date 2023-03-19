#cw 3.1

word = input('Podaj słowo: ')

edge = '+' + len(word)*'---+'
S = '|' #lewa krawędź wiersza ze słowem

for char in word:
    S += '{}|'.format(char.center(3))

print(edge) 
print(S)
print(edge) 

#eof
