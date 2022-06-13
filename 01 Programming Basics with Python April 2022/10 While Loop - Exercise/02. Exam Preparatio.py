bad_grades_threshold = int(input())

problem_counter = 0
last_problem = ''
bad_grades_counter = 0
total_grades = 0
has_failed = False

while bad_grades_counter < bad_grades_threshold:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break
    problem_grade = int(input())
    if problem_grade <= 4:
        bad_grades_counter +=1
    if bad_grades_counter == bad_grades_threshold:
        has_failed = True
        break
    problem_counter += 1
    last_problem = problem_name
    total_grades += problem_grade

if has_failed:
    print(f"You need a break, {bad_grades_counter} poor grades.")
else:
    average_grades = total_grades / problem_counter
    print(f"Average score: {average_grades:.2f}")
    print(f"Number of problems: {problem_counter}")
    print(f"Last problem: {last_problem}")