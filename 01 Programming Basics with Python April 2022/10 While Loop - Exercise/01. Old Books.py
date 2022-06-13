fav_book = input()
curr_book = input()
is_found = False
counter = 0
while curr_book != 'No More Books':
    if curr_book == fav_book:
        is_found = True
        break
    counter +=1
    curr_book = input()

if is_found:
    print(f'You checked {counter} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {counter} books.')