n = int(input())
max = -10000000
min = 10000000
for i in range(n):
    a = int(input())
    if a > max:
        max = a
    if a < min:
        min = a

print(f'Max number: {max}')
print(f'Min number: {min}')