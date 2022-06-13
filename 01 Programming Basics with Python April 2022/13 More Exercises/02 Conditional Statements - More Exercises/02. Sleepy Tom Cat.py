holidays = int(input())
working_days = 365 - holidays
play_time = working_days*63 + holidays*127
if play_time>30000:
    print('Tom will run away')
    print(f'{(play_time-30000)//60} hours and {(play_time-30000)%60} minutes more for play')
else:
    print('Tom sleeps well')
    print(f'{(30000-play_time)//60} hours and {(30000-play_time)%60} minutes less for play')