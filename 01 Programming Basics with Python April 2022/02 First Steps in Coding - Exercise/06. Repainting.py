amount_nailon = int(input())
amount_paint = int(input())
amount_razreditel = int(input())
hours = int(input())

total_materials = (amount_nailon+2) * 1.5 + (amount_paint + amount_paint*0.1) * 14.5 + amount_razreditel * 5 + 0.4
total = total_materials + total_materials*0.3*hours
print(total)