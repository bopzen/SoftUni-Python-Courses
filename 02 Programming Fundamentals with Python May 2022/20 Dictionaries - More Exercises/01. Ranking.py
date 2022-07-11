contest_passwords = {}
submissions = {}

while True:
    command = input()
    if command == 'end of contests':
        break
    list_command = command.split(":")
    contest, password = list_command[0], list_command[1]
    contest_passwords[contest] = password

while True:
    command = input()
    if command == 'end of submissions':
        break
    list_command = command.split("=>")
    contest, password, username, points = list_command[0], list_command[1], list_command[2], int(list_command[3])
    if contest in contest_passwords and password in contest_passwords.values():
        if username not in submissions:
            submissions[username] = {}
            submissions[username][contest] = points
        else:
            if contest in submissions[username]:
                if points > submissions[username][contest]:
                    submissions[username][contest] = points
            else:
                submissions[username][contest] = points

max_total = 0
max_username = ""

for key, value in submissions.items():
    total = 0
    for nested_value in value.values():
        total += nested_value
    if total > max_total:
        max_total = total
        max_username = key
print(f"Best candidate is {max_username} with total {max_total} points.")
print("Ranking:")

for key, value in sorted(submissions.items()):
    print(key)
    for nested_key, nested_value in sorted(value.items(), key=lambda x:x[1], reverse=True):
        print(f"#  {nested_key} -> {nested_value}")
