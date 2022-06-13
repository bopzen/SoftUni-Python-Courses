jury_count = int(input())
count_grades = 0
sum_presentation_grades = 0
sum_total_grades = 0
while True:
    presentation = input()
    if presentation == 'Finish':
        break
    for i in range(jury_count):
        grade = float(input())
        sum_presentation_grades += grade
        sum_total_grades += grade
        count_grades += 1
    average_presentation_grade = sum_presentation_grades / jury_count
    print(f"{presentation} - {average_presentation_grade:.2f}.")
    sum_presentation_grades = 0

average_grade = sum_total_grades / count_grades
print(f"Student's final assessment is {average_grade:.2f}.")