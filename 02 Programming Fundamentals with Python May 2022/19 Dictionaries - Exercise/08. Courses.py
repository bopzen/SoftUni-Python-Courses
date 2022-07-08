courses_dict = {}

while True:
    command = input()
    if command == 'end':
        break
    command = command.split(" : ")
    course_name, student_name = command[0], command[1]
    if course_name not in courses_dict:
        courses_dict[course_name] = [student_name]
    else:
        courses_dict[course_name].append(student_name)

for key, value in courses_dict.items():
    print(f"{key}: {len(courses_dict[key])}")
    for element in value:
        print(f"-- {element}")