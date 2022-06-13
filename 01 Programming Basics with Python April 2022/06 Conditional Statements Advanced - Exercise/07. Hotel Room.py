month = input()
nights = int(input())
apt_price = 0
studio_price = 0
if month == 'May' or month == 'October':
    studio_price = 50 * nights
    apt_price = 65 * nights
    if nights > 14:
        studio_price -= studio_price * 0.3
        apt_price -= apt_price * 0.1
    elif nights >7:
        studio_price -= studio_price * 0.05
elif month == 'June' or month == 'September':
    studio_price = 75.2 * nights
    apt_price = 68.7 * nights
    if nights > 14:
        studio_price -= studio_price * 0.2
        apt_price -= apt_price * 0.1
elif month == 'July' or month == 'August':
    studio_price = 76 * nights
    apt_price = 77 * nights
    if nights > 14:
        apt_price -= apt_price * 0.1
print(f'Apartment: {apt_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')