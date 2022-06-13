turns = int(input())
points = 0
invalid_num = 0
num_40 = 0
num_30 = 0
num_20 = 0
num_10 = 0
num_0 = 0
for i in range(turns):
    num = int(input())
    if num >50 or num <0:
        points /= 2
        invalid_num +=1
    elif num >=40:
        points += 100
        num_40 +=1
    elif num >=30:
        points += 50
        num_30 += 1
    elif num >=20:
        points += num*0.4
        num_20 += 1
    elif num >=10:
        points += num*0.3
        num_10 += 1
    elif num >=0:
        points += num*0.2
        num_0 += 1
perc_num40 = num_40 / turns * 100
perc_num30 = num_30 / turns * 100
perc_num20 = num_20 / turns * 100
perc_num10 = num_10 / turns * 100
perc_num0 = num_0 / turns * 100
perc_invalid = invalid_num / turns * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {perc_num0:.2f}%")
print(f"From 10 to 19: {perc_num10:.2f}%")
print(f"From 20 to 29: {perc_num20:.2f}%")
print(f"From 30 to 39: {perc_num30:.2f}%")
print(f"From 40 to 50: {perc_num40:.2f}%")
print(f"Invalid numbers: {perc_invalid:.2f}%")