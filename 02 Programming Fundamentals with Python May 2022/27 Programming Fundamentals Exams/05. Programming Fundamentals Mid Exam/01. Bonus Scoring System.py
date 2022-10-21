import math

students = int(input())
lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_bonus_student_attendances = 0
for i in range(students):
    attendances = int(input())
    total_bonus = attendances / lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        max_bonus_student_attendances =  attendances
max_bonus =  math.ceil(max_bonus)
max_bonus_student_attendances = math.ceil(max_bonus_student_attendances)
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {max_bonus_student_attendances} lectures.")