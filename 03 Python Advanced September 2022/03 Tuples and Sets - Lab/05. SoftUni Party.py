guests_number = int(input())
guest_list = set()
for _ in range(guests_number):
    guest_list.add(input())
command = input()
while command != 'END':
    guest_list.remove(command)
    command = input()
print(len(guest_list))
vip = []
regular = []
for guest in guest_list:
    if guest[0].isdigit():
        vip.append(guest)
    elif guest[0].isalpha():
        regular.append(guest)
if vip:
    print('\n'.join(sorted(vip)))
if regular:
    print('\n'.join(sorted(regular)))