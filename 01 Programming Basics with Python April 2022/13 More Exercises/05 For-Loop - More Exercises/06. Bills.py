months = int(input())
total_electric_bill = 0
total_water = 0
total_internet = 0
total_others = 0

for i in range(months):
    electric_bill = float(input())
    total_electric_bill += electric_bill
    total_water += 20
    total_internet += 15
    total_others += electric_bill + 20 + 15 + (electric_bill + 20 + 15) * 0.2

total_bills = total_electric_bill + total_water + total_internet + total_others
average_bills = total_bills / months

print(f"Electricity: {total_electric_bill:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {total_others:.2f} lv")
print(f"Average: {average_bills:.2f} lv")