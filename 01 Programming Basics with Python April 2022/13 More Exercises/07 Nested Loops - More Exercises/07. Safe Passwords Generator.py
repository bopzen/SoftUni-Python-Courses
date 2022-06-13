max_passwords = int(input())
combinations_counter = 1
is_finished = False
symbol_a = 35
symbol_b = 64
x = 1
y = 1

for x in range(1, a+1):
    for y in range(1, b+1):
        print(f'{chr(symbol_a)}{chr(symbol_b)}{x}{y}{chr(symbol_b)}{chr(symbol_a)}',end='|')
        if symbol_a == 55:
            symbol_a = 35
        else:
            symbol_a += 1
        if symbol_b == 96:
            symbol_b = 64
        else:
            symbol_b += 1
        if combinations_counter == max_passwords or (x==a and y==b):
            is_finished = True
            break
        else:
            combinations_counter +=1
    if is_finished:
        break