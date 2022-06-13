import math

name = input()
time_series = int(input())
time_break = int(input())
time_break-=time_break/8 + time_break/4
if time_break>=time_series:
    print(f'You have enough time to watch {name} and left with {math.ceil(time_break-time_series)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {name}, you need {math.ceil(time_series-time_break)} more minutes.')