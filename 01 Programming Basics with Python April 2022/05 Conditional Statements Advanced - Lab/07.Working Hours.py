hour = int(input())
day = input()
working_days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
if hour >=10 and hour <=18:
    if day in working_days:
        print('open')
    elif day == 'Sunday':
        print('closed')
else:
    print('closed')