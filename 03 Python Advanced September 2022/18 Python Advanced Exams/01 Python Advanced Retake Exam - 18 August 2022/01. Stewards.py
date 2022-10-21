from collections import deque

seats = input().split(", ")
first_numbers = deque(list(map(int, input().split(", "))))
second_numbers = list(map(int, input().split(", ")))
seat_matches = []
rotations_count = 0

for rotations_count in range(1, 11):
    current_first_number = first_numbers.popleft()
    current_second_number = second_numbers.pop()
    sum_ascii = current_first_number + current_second_number
    check_seat1 = str(current_first_number) + chr(sum_ascii)
    check_seat2 = str(current_second_number) + chr(sum_ascii)
    if check_seat1 in seat_matches or check_seat2 in seat_matches:
        continue
    elif check_seat1 in seats:
        seat_matches.append(check_seat1)
    elif check_seat2 in seats:
        seat_matches.append(check_seat2)
    else:
        first_numbers.append(current_first_number)
        second_numbers.insert(0, current_second_number)
    if len(seat_matches) == 3:
        break
print(f'Seat matches: {", ".join([seat for seat in seat_matches])}')
print(f'Rotations count: {rotations_count}')