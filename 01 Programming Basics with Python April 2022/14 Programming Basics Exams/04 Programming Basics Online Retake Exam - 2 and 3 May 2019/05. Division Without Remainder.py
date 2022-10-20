n = int(input())
p1 = 0
p2 = 0
p3 = 0
for i in range(n):
    number = int(input())
    if number % 2 == 0:
        p1 +=1
    if number % 3 == 0:
        p2 +=1
    if number % 4 == 0:
        p3 +=1
perc1 = p1/n*100
perc2 = p2/n*100
perc3 = p3/n*100
print(f"{perc1:.2f}%")
print(f"{perc2:.2f}%")
print(f"{perc3:.2f}%")
