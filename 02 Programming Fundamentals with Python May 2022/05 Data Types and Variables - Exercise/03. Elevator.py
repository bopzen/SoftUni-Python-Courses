people = int(input())
capacity = int(input())

full_courses = people // capacity
remaining_people = people % capacity
if full_courses == 0:
    print(1)
else:
    if remaining_people != 0:
        print(full_courses + 1)
    else:
        print(full_courses)