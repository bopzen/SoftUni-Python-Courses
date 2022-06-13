n = int(input())
print('+ ' + '- '*(n-2) + '+')
for row in range(1, n-1):
    print('|', end=' ')
    for col in range(1, n-1):
        print('-',end=' ')
    print('|')

print('+ ' + '- '*(n-2) + '+')