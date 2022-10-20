visitors = int(input())
back = 0
chest = 0
legs = 0
abs_m = 0
shake = 0
bar = 0
workout = 0
for i in range(visitors):
    action = input()
    if action == 'Back':
        back +=1
        workout +=1
    elif action == 'Chest':
        chest +=1
        workout +=1
    elif action == 'Legs':
        legs +=1
        workout +=1
    elif action == 'Abs':
        abs_m +=1
        workout +=1
    elif action == 'Protein shake':
        shake +=1
    elif action == 'Protein bar':
        bar +=1
proteins = visitors - workout
workout_perc = workout / visitors * 100
proteins_perc = proteins / visitors * 100

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs_m} - abs")
print(f"{shake} - protein shake")
print(f"{bar} - protein bar")
print(f"{workout_perc:.2f}% - work out")
print(f"{proteins_perc:.2f}% - protein")

