phone_book = {}
while True:
    command = input()
    if "-" not in command:
        break
    command = command.split("-")
    name, number = command[0], command[1]
    phone_book[name] = number

n = int(command)
for i in range(n):
    search_name = input()
    if search_name not in phone_book:
        print(f"Contact {search_name} does not exist.")
    else:
        print(f"{search_name} -> {phone_book[search_name]}")