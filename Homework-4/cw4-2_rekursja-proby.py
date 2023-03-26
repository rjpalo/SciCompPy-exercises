#cw 4-2 / rekursja proby

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#proba 1

def reverse_range_1(L, left, right):
    '''reverse part of a list in place; numbers outside range are unchanged'''

    if 0 <= left < len(L) and 0 <= right < len(L):
        beg = L[:left]
        S = L[left:right + 1] #slice of interest
        end = L[right + 1:]

        i = 0
        while i < len(S):
            if S[i] == L[left]:
                S[i] = L[right]
            else:
                S[i] = L[right - i]
            i += 1

        L = beg + S + end
        return L
    else:
        return 'chosen range at least partially outside of given list'


#check
print('Original list: {}'.format(L))
print('Partially reversed list: {}'.format(reverse_range_1(L, 3, 6)))

#proba 2

def reverse_range_2(L, left, right):
    '''reverse part of a list in place; numbers outside range are unchanged'''

    if 0 <= left < len(L) and 0 <= right < len(L):
        i = 0
        a = L[left]
        b = L[right]

        while i < (len(L[left:right + 1]) // 2): # // 2 unika podwójnej zamiany
            a = L[left + i]
            b = L[right - i]
            L[left + i], L[right - i] = b, a
            i += 1      

        return L
    else:
        return 'chosen range at least partially outside of given list'


#check
print('Original list: {}'.format(L))
print('Partially reversed list: {}'.format(reverse_range_2(L, 3, 6)))

#eof
