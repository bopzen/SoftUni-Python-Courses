students = {}

while True:
    command = input()
    if ":" not in command:
        break
    list_command = command.split(":")
    name, id, course = list_command[0], list_command[1], list_command[2]
    if course not in students:
        students[course] = {}
    students[course][id] = name

course = " ".join(command.split("_"))

for key, value in students.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")