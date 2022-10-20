destination = input()
dates = input()
count_nights = int(input())
cost = 0
if destination == 'France':
    if dates == '21-23':
        cost = count_nights * 30
    elif dates == '24-27':
        cost = count_nights * 35
    elif dates == '28-31':
        cost = count_nights * 40
elif destination == 'Italy':
    if dates == '21-23':
        cost = count_nights * 28
    elif dates == '24-27':
        cost = count_nights * 32
    elif dates == '28-31':
        cost = count_nights * 39
elif destination == 'Germany':
    if dates == '21-23':
        cost = count_nights * 32
    elif dates == '24-27':
        cost = count_nights * 37
    elif dates == '28-31':
        cost = count_nights * 43
print(f'Easter trip to {destination} : {cost:.2f} leva.')