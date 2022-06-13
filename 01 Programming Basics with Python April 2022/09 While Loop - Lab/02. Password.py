username = input()
password = input()

entry = input()
while entry != password:
    entry = input()
print(f"Welcome {username}!")