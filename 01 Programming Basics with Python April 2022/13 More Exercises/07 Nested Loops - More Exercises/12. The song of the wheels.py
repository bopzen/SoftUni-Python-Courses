m = int(input())
counter = 0
password = ''
is_found = False
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1,10):
                if a < b and c > d and (a * b + c * d == m):
                    counter += 1
                    print(a,b,c,d,sep='', end=' ')
                    if counter == 4:
                        is_found = True
                        password = str(a) + str(b) + str(c) + str(d)
if is_found:
    print()
    print(f'Password: {password}')
elif not is_found:
    print()
    print('No!')
elif counter == 0:
    print('No!')