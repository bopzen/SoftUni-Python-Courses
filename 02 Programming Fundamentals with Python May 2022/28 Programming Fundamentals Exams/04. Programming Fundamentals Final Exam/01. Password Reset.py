
initial_password = input()
password = initial_password
while True:
    command = input()
    if command == 'Done':
        break
    tokens = command.split()
    if tokens[0] == 'TakeOdd':
        new_password = ""
        for i in range(1, len(password),2):
            new_password += password[i]
        password = new_password
        print(password)
    elif tokens[0] == 'Cut':
        index, length = int(tokens[1]), int(tokens[2])
        substring = password[index: index+length]
        password = password.replace(substring,"",1)
        print(password)
    elif tokens[0] == 'Substitute':
        substring, substitute = tokens[1], tokens[2]
        if substring not in password:
            print("Nothing to replace!")
        else:
            while substring in password:
                password = password.replace(substring, substitute)
            print(password)

print(f"Your password is: {password}")

