#cw 5-2

#Create the function print_working_days(date1, date2), where 'date1' and
#'date2' are strings of the form 'YYYY-MM-DD'. The function prints dates of
#working days (from Monday to Friday) in the given range, 'date2' is excluded.

import datetime

def print_working_days(date1, date2):
    '''return Mon-Fri dates from given date range; date1, date2 = YYYY-MM-DD'''
    
    start = datetime.date.fromisoformat(date1)
    end = datetime.date.fromisoformat(date2)
    td = datetime.timedelta(days = 1)
    
    n_workday = 0
    workdays = []

    while start < end: #finds working days in range
        if start.isoweekday() < 6:
            n_workday += 1
            workdays.append(start)
        start += td

    #ładna tabelka. robię sama bo nie mogę znaleźc 'pretty table' na razie

    day_dict = {1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri', 6:'Sat', 7:'Sun'}
    L1 = '+---------------+-----+'
    L2 = '|{}|{}|'.format('date'.center(15), 'day'.center(5))

    print(L1, L2, L1, sep = '\n')
    for day in workdays:
        print('|{}|{}|'.format(day.isoformat().center(15),
                               day_dict[day.isoweekday()].center(5)))
    print(L1)
    
    return print('Working days total: {}'.format(n_workday))

     

#check
print_working_days('2023-03-29', '2023-04-07')
print(30*'*')
print_working_days('2023-12-13', '2024-02-01')

input('Naciśnij klawisz: ')
#eof
