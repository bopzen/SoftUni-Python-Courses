employee1_help_per_hour = int(input())
employee2_help_per_hour = int(input())
employee3_help_per_hour = int(input())
students = int(input())
hours = 0
all_help_per_hour = employee1_help_per_hour + employee2_help_per_hour + employee3_help_per_hour
while students > 0:
    hours += 1
    if hours % 4 == 0 :
        continue
    else:
        students -= all_help_per_hour
print(f'Time needed: {hours}h.')
