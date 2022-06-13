season = input()
group_type = input()
count_students = int(input())
count_nights = int(input())
total_price = 0
discount = 0
sport = ''
if season == 'Winter':
    if group_type == 'boys':
        total_price = count_students * count_nights * 9.6
        sport = 'Judo'
    elif group_type == 'girls':
        total_price = count_students * count_nights * 9.6
        sport = 'Gymnastics'
    elif group_type == 'mixed':
        total_price = count_students * count_nights * 10
        sport = 'Ski'
elif season == 'Spring':
    if group_type == 'boys':
        total_price = count_students * count_nights * 7.2
        sport = 'Tennis'
    elif group_type == 'girls':
        total_price = count_students * count_nights * 7.2
        sport = 'Athletics'
    elif group_type == 'mixed':
        total_price = count_students * count_nights * 9.5
        sport = 'Cycling'
elif season == 'Summer':
    if group_type == 'boys':
        total_price = count_students * count_nights * 15
        sport = 'Football'
    elif group_type == 'girls':
        total_price = count_students * count_nights * 15
        sport = 'Volleyball'
    elif group_type == 'mixed':
        total_price = count_students * count_nights * 20
        sport = 'Swimming'
if count_students >=50:
    discount = 0.5
elif count_students >=20:
    discount = 0.15
elif count_students >=10:
    discount = 0.05
total_price -= total_price*discount
print(f'{sport} {total_price:.2f} lv.')