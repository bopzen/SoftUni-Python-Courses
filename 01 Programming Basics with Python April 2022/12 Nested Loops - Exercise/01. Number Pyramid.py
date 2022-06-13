n = int(input())
counter = 1
flag = False
for i in range(1,n+1):
    for j in range(1,i+1):
        print(counter, end = ' ')
        if counter == n:
            flag = True
            break
        counter +=1
    if flag:
        break
    print()