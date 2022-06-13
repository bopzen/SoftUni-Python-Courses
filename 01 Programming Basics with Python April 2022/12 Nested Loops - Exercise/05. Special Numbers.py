n = int(input())
is_special = True
for i in range(1111,10000):
    number = str(i)
    is_special = True
    for c in number:
        if int(c) == 0:
            is_special = False
            break
        if n % int(c) != 0:
            is_special = False
            break
    if is_special:
        print(i,end = ' ')