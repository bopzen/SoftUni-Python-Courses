list_lessons = input().split(", ")

while True:
    command = input()
    if command == 'course start':
        break
    list_command = command.split(":")
    action = list_command[0]
    if action == 'Add':
        lesson = list_command[1]
        if lesson not in list_lessons:
            list_lessons.append(lesson)
    elif action == 'Insert':
        lesson = list_command[1]
        index = int(list_command[2])
        if lesson not in list_lessons:
            list_lessons.insert(index, lesson)
    elif action == 'Remove':
        lesson = list_command[1]
        exercise = lesson + "-Exercise"
        if lesson in list_lessons:
            list_lessons.remove(lesson)
        if exercise in list_lessons:
            list_lessons.remove(exercise)
    elif action == 'Swap':
        lesson1 = list_command[1]
        lesson2 = list_command[2]
        exercise1 = lesson1 + "-Exercise"
        exercise2 = lesson2 + "-Exercise"
        if lesson1 in list_lessons and lesson2 in list_lessons:
            index_lesson1 = list_lessons.index(lesson1)
            index_lesson2 = list_lessons.index(lesson2)
            list_lessons[index_lesson1], list_lessons[index_lesson2] = list_lessons[index_lesson2] , list_lessons[index_lesson1]
        if exercise1 in list_lessons:
            index_lesson1 = list_lessons.index(lesson1)
            index_exercise1 = list_lessons.index(exercise1)
            list_lessons.pop(index_exercise1)
            list_lessons.insert(index_lesson1+1,exercise1)
        if exercise2 in list_lessons:
            index_lesson2 = list_lessons.index(lesson2)
            index_exercise2 = list_lessons.index(exercise2)
            list_lessons.pop(index_exercise2)
            list_lessons.insert(index_lesson2 + 1, exercise2)
    elif action == 'Exercise':
        lesson = list_command[1]
        exercise = lesson + "-Exercise"
        if lesson in list_lessons and exercise not in list_lessons:
            index_lesson = list_lessons.index(lesson)
            list_lessons.insert(index_lesson+1,exercise)
        elif lesson not in list_lessons:
            list_lessons.append(lesson)
            list_lessons.append(exercise)
for index in range(len(list_lessons)):
    print(str(index+1) + "." + list_lessons[index])