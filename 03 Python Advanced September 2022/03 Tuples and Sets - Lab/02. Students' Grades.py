students_count = int(input())

student_grades = {}

for _ in range(students_count):
    name, grade = input().split()
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(float(grade))

for name, grades in student_grades.items():
    str_grades = ' '.join(f'{grade:.2f}' for grade in grades)
    print(f'{name} -> {str_grades} (avg: {sum(grades)/len(grades):.2f})')