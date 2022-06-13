name = input()
year = 0
counter = 0
total_grades = 0
while True:
    annual_grade = float(input())
    year += 1
    if annual_grade < 4:
        counter +=1
        if counter == 2:
            print(f"{name} has been excluded at {year} grade")
            break
        year -=1
    else:
        total_grades += annual_grade
    if year == 12:
        print(f"{name} graduated. Average grade: {total_grades/12:.2f}")
        break