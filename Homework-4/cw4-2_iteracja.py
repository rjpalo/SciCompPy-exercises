#cw 4-2 / iterative version

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def reverse_range(L, left, right):
    '''reverse part of a list in place; numbers outside range are unchanged'''

    if 0 <= left < len(L) and 0 <= right < len(L):
        beg = L[:left]
        S = L[left:right + 1] #slice of interest
        end = L[right + 1:]
    
        i = len(S) #idziemy od końca
        rev_S = []
    
        while i > 0:
            rev_S.append(S[i-1])
            i -= 1
    
        L = beg + rev_S + end
        return L
    else:
        return 'chosen range at least partially outside of given list'


#check
print('Original list: {}'.format(L))
print('Partially reversed list: {}'.format(reverse_range(L, 3, 6)))

#eof

