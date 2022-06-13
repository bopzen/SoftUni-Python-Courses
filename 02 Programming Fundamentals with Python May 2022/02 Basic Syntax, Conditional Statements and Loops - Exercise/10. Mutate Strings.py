first_string = input()
second_string = input()
previous_string = first_string

for c1 in range(1, len(second_string)+1):
    new_string = ''
    for c2 in range(c1):
        new_string = new_string + second_string[c2]
    for c3 in range(c1,len(first_string)):
        new_string = new_string + first_string[c3]
    if new_string == previous_string:
        continue
    else:
        previous_string = new_string
        print(new_string)