parking_dict = {}
n = int(input())
for i in range(n):
    command = input().split()
    if command[0] == 'register':
        username, license_plate = command[1], command[2]
        if username not in parking_dict:
            parking_dict[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif command[0] == 'unregister':
        username = command[1]
        if username in parking_dict:
            del parking_dict[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")
print("\n".join(f"{key} => {value}" for key, value in parking_dict.items()))