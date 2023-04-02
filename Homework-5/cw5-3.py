#cw 5-3

#Create the generator random_walk(start) for a 1D random walker.If a position
#at a certain moment is x, then the next position can be x+1 or x-1 with equal
#probabilities. Find the final position after 100 moves (start=0).
#Repeat experiments.

import random
from prettytable import PrettyTable

def random_walk(start):
    '''1D random walker generator'''     
  
    while True:
        yield start
        s = random.choice([-1, 1])
        start += s
        

#check; 5 tries

rw1 = random_walk(0)
rw2 = random_walk(0)
rw3 = random_walk(0)
rw4 = random_walk(0)
rw5 = random_walk(0)

results = PrettyTable()
results.field_names = ['step no.', 'position (1)', 'position (2)',
                       'position (3)', 'position (4)', 'position (5)']

for i in range(101):
    results.add_row([i, next(rw1), next(rw2), next(rw3), next(rw4), next(rw5)])

print(results)   


input('Naciśnij klawisz: ')
#eof
    
    
