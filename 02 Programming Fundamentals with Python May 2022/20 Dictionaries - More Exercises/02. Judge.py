contest_submissions = {}
users_submissions_points = {}

while True:
    command = input()
    if command == 'no more time':
        break
    list_command = command.split(" -> ")
    username, contest, points = list_command[0], list_command[1], int(list_command[2])
    if contest not in contest_submissions:
        contest_submissions[contest] = {}
        contest_submissions[contest][username] = points
    else:
        if username in contest_submissions[contest]:
            if points > contest_submissions[contest][username]:
                contest_submissions[contest][username] = points
        else:
            contest_submissions[contest][username] = points

for key, value in contest_submissions.items():
    for nested_key, nested_value in value.items():
        if nested_key not in users_submissions_points:
            users_submissions_points[nested_key] = nested_value
        else:
            users_submissions_points[nested_key] += nested_value


for key,value in contest_submissions.items():
    print(f"{key}: {len(contest_submissions[key])} participants")
    counter = 1
    for nested_key, nested_value in sorted(value.items(), key=lambda x:(-x[1],x[0])):
        print(f"{counter}. {nested_key} <::> {nested_value} ")
        counter += 1

print("Individual standings:")
counter = 1
for key, value in sorted(users_submissions_points.items(), key=lambda x:(-x[1],x[0])):
    print(f"{counter}. {key} -> {value}")
    counter += 1

