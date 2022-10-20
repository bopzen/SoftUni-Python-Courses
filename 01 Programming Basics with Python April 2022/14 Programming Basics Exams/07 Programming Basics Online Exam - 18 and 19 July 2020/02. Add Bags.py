price_luggage = float(input())
weight_luggage = float(input())
days_to_trip = int(input())
count_luggage = int(input())
charge = 0
if weight_luggage >20:
    manual_price = float(input())
    charge = manual_price * count_luggage
elif weight_luggage >=10:
    charge = price_luggage * count_luggage * 0.5
else:
    charge = price_luggage * count_luggage * 0.2

if days_to_trip > 30:
    charge += charge * 0.1
elif days_to_trip >= 7:
    charge += charge * 0.15
else:
    charge += charge * 0.4
print(f"The total price of bags is: {charge:.2f} lv.")