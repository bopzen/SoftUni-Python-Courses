w = float(input())
h = float(input())

count_desks = (w*100//120) * ((h-1)*100//70) -3
print(count_desks)