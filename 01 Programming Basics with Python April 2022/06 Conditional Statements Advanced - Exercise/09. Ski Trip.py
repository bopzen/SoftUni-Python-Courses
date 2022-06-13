days_stay = int(input())
room_type = input()
rate = input()
nights = days_stay - 1
total_price = 0
discount = 0
rate_tip_discount = 0
if days_stay > 15:
    if room_type == 'apartment':
        discount = 0.5
        total_price = nights * 25
    elif room_type == 'president apartment':
        discount = 0.2
        total_price = nights * 35
    elif room_type == 'room for one person':
        total_price = nights * 18
elif days_stay >=10:
    if room_type == 'apartment':
        discount = 0.35
        total_price = nights * 25
    elif room_type == 'president apartment':
        discount = 0.15
        total_price = nights * 35
    elif room_type == 'room for one person':
        total_price = nights * 18
else:
    if room_type == 'apartment':
        discount = 0.3
        total_price = nights * 25
    elif room_type == 'president apartment':
        discount = 0.1
        total_price = nights * 35
    elif room_type == 'room for one person':
        total_price = nights * 18
total_price -= total_price*discount
if rate == 'positive':
    total_price += total_price*0.25
elif rate == 'negative':
    total_price -= total_price * 0.1
print(f'{total_price:.2f}')