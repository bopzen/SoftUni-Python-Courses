count_chrysanthemums = int(input())
count_roses= int(input())
count_tulips = int(input())
season = input()
is_holiday = input()
total_price = 0
count_flowers = count_roses + count_tulips + count_chrysanthemums
if season == 'Spring' or season == 'Summer':
    total_price = count_chrysanthemums * 2 + count_roses * 4.1 + count_tulips * 2.5
elif season == 'Autumn' or season == 'Winter':
    total_price = count_chrysanthemums * 3.75 + count_roses * 4.5 + count_tulips * 4.15
if is_holiday == 'Y':
    total_price += total_price * 0.15
if count_tulips >=7 and season == 'Spring':
    total_price -= total_price * 0.05
if count_roses >=10 and season == 'Winter':
    total_price -= total_price * 0.1
if count_flowers >= 20:
    total_price -= total_price * 0.2
total_price += 2
print(f'{total_price:.2f}')