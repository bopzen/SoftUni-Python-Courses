import math
count_people = int(input())
entrance_fee = float(input())
price_sunbed = float(input())
price_umbrella = float(input())

total_entrance_fee = count_people * entrance_fee
sunbeds = math.ceil(count_people * 0.75)
umbrellas = math.ceil(count_people /2)
price_sunbeds_and_umbrella = sunbeds * price_sunbed + umbrellas * price_umbrella
total = total_entrance_fee + price_sunbeds_and_umbrella

print(f'{total:.2f} lv.')