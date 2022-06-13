start_number = int(input())
end_number = int(input())

for num1 in range(start_number,end_number+1):
    for num2 in range(start_number, end_number + 1):
        for num3 in range(start_number, end_number + 1):
            for num4 in range(start_number, end_number + 1):
                if (num1 % 2 == 0 and num4 % 2 !=0) or (num4 % 2 == 0 and num1 % 2 !=0):
                    if num1 > num4 and (num2+num3) % 2 == 0:
                        print(num1,num2,num3,num4, sep='', end=' ')