day = input()
working_day = ['Monday','Tuesday','Wednesday','Thursday','Friday']
weekend = ['Saturday', 'Sunday']
if day in working_day:
    print('Working day')
elif day in weekend:
    print('Weekend')
else:
    print('Error')