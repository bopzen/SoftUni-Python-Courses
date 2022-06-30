class Party:
    def __init__(self):
        self.people = []


party = Party()
while True:
    command = input()
    if command == 'End':
        break
    name = command
    party.people.append(name)

print("Going: " + ", ".join(party.people))
print("Total: " + str(len(party.people)))