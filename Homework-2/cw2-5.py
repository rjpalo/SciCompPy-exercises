#cw 2.5

S = str(input('Podaj string: ')) 
black_count = 0
white_count = 0

for char in S:
    if  char.isspace():
        white_count += 1
    else:
        black_count += 1
        
print('Liczba czarnych znaków w stringu to {}.'.format(black_count))

words = S.split() #word list, splits on whitespace
print('Liczba słów w stringu to {}.'.format(len(words)))

longest_word = max(words, key=len)
print('Najdłuższe słowo w stringu to "{}", o długości \
{} znaków.'.format(longest_word, len(longest_word)), end = '\n\n')

lexi_list = sorted(words, key = str.lower) #lexi sorting
print('Słowa posortowane w kolejności alfabetycznej:')
print(lexi_list, end = '\n\n')

length_list = sorted(words, key = len) #length sorting
print('Słowa posortowane wg długości:')
print(length_list)
