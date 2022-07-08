submissions_dict = {}
list_banned = []
languages_dict = {}
while True:
    command = input()
    if command == 'exam finished':
        break
    list_command = command.split("-")
    username = list_command[0]
    if 'banned' in list_command:
        list_banned.append(username)
    else:
        language, points = list_command[1], int(list_command[2])
        if language not in languages_dict:
            languages_dict[language] = 1
        else:
            languages_dict[language] += 1
        if username not in submissions_dict:
            submissions_dict[username] = {}
            submissions_dict[username][language] = points
        else:
            if language in submissions_dict[username]:
                if points > submissions_dict[username][language]:
                    submissions_dict[username][language] = points
            else:
                submissions_dict[username][language] = points

print("Results:")
for key, value in submissions_dict.items():
    for nested_key, nested_value in value.items():
        if key not in list_banned:
            print(f"{key} | {nested_value}")
print("Submissions:")
for key, value in languages_dict.items():
    print(f"{key} - {value}")