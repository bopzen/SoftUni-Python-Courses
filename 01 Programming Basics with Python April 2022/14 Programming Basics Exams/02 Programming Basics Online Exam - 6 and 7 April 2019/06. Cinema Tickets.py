student_tickets = 0
standard_tickets = 0
kids_tickets = 0
total_tickets = 0
flag = False
while True:
    movie = input()
    if movie == 'Finish':
        break
    seats = int(input())
    sold_tickets = 0
    while sold_tickets < seats :
        ticket_type = input()
        if ticket_type == 'End':
            break
        sold_tickets += 1
        total_tickets += 1
        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kids_tickets += 1
    print(f"{movie} - {sold_tickets/seats*100:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets/total_tickets*100:.2f}% student tickets.")
print(f"{standard_tickets/total_tickets*100:.2f}% standard tickets.")
print(f"{kids_tickets/total_tickets*100:.2f}% kids tickets.")


