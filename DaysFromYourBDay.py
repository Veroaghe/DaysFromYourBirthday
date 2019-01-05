# What is the [insert number] day after your birthday?
# Find out with this script.

import datetime as dt

# Makes the user fill in a valid date
date = True
while date:
    y = input('What is your birthyear? (max. 4 digit number): ')
    m = input('What is your birthmonth? (number from 1 to 12): ')
    d = input('What is your birthday? (number from 1 to 31): ')
    
    try:
        bday = dt.date(int(y), int(m), int(d))
        date = False
    
    except:
        print('\nPlease enter valid integer numbers to move on.\n')

# Calculates the largest number of days you can input
maxdate = dt.date(9999, 12, 31)
maxordinal = maxdate.toordinal()
ordinal = bday.toordinal()
maxint = maxordinal - ordinal + 1

# A loop that gives the user the chance to enter differen day amounts
while True:
    print('\nWhich day after your B-day do you want to calculate? (0 < integer < {0})'.format(maxint))
    n = input('Or, end this loop with the word "stop": ')

    if n == 'stop':
        break

    else:
        try:
            if int(n) >= int(maxint):
                raise Exception
            n = int(n)

            if n <= 0:
                print('\nEither enter an integer bigger than 0 and smaller than {0} or the word "stop".'.format(maxint))
           
            else:
                newordinal = int(ordinal) + int(n)
                print('\n============================================================='+'='*len(str(n)))
                print('{0} days from your birthday on {2} is the day {1}'.format(n, bday.fromordinal(newordinal), bday.isoformat()))
                print('============================================================='+'='*len(str(n)))
       
        except:
            print('\nEither enter an integer bigger than 0 and smaller than {0} or the word "stop".'.format(maxint))

