last_sector = input()
rows = int(input())
odd_row_seats = int(input())
count_seats = 0
for sector in range(ord('A'), ord(last_sector)+1):
    for row in range(1,rows+1):
        if row % 2 != 0:
            for seat in range(ord('a'),ord('a')+odd_row_seats):
                print(f"{chr(sector)}{row}{chr(seat)}")
                count_seats +=1
        else:
            for seat in range(ord('a'),ord('a')+odd_row_seats + 2):
                print(f"{chr(sector)}{row}{chr(seat)}")
                count_seats += 1
    rows +=1
print(count_seats)