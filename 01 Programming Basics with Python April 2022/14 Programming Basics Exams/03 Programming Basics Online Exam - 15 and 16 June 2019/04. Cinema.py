seats = int(input())
profit = 0
is_full = False
while True:
    command = input()
    if command == 'Movie time!':
        break
    people = int(command)
    if people > seats:
        is_full = True
        print("The cinema is full.")
        break
    profit += people * 5
    if people % 3 == 0:
        profit -= 5
    seats -= people

if not is_full:
    print(f"There are {seats} seats left in the cinema.")
print(f"Cinema income - {profit} lv.")

