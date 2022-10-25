n = int(input())


def print_row(row):
    for i in range(n - row):
        print(' ', end='')
    for i in range(row):
        print('*', end=' ')
    print()


for i in range(1, n):
    print_row(i)
for i in range(n, 0 , -1):
    print_row(i)