count_students = int(input())

top_grade = 0
good_grade = 0
average_grade = 0
weak_grade = 0
sum_grades = 0
for i in range(count_students):
    grade = float(input())
    sum_grades += grade
    if grade >= 5:
        top_grade +=1
    elif grade >=4:
        good_grade +=1
    elif grade >=3:
        average_grade +=1
    else:
        weak_grade +=1
average = sum_grades / count_students
top_perc = top_grade / count_students * 100
good_perc = good_grade / count_students * 100
average_perc = average_grade / count_students * 100
weak_perc = weak_grade / count_students * 100

print(f"Top students: {top_perc:.2f}%")
print(f"Between 4.00 and 4.99: {good_perc:.2f}%")
print(f"Between 3.00 and 3.99: {average_perc:.2f}%")
print(f"Fail: {weak_perc:.2f}%")
print(f"Average: {average:.2f}")