#cw 5-1
#For a given directory (top) find the number of bytes taken by PDF files in
#the directory tree (".pdf" extensions). The code should be in the function
#find_pdf_size(top). In order to test the current directory we run
#find_pdf_size(".").

import os

def find_pdf_size(top):
    '''return number and total size of pdf files in top directory'''

    n_pdf = 0
    pdf_size = 0
    for root, dirs, files in os.walk(top): #top-down
        for name in files:
            if name.lower().endswith('.pdf'): #.pdf + .PDF files
                n_pdf += 1
                pdf_size += os.path.getsize((os.path.join(root, name)))

    return 'The {} pdf files in this directory take up {} bytes.'.format(
        n_pdf, pdf_size)


#check
top1 = '.'
top2 = str(input('podaj ścieżkę: '))

print('test 1. current dir: ', find_pdf_size(top1))
print('test 2. ścieżka własna: ', find_pdf_size(top2))


input('naciśnij klawisz: ')
#eof
