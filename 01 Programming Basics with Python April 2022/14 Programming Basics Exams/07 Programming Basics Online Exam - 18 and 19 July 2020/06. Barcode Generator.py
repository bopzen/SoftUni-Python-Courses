start_number = int(input())
end_number = int(input())

for num1 in range(start_number//1000, (end_number//1000)+1):
    for num2 in range(start_number//100%10, (end_number//100%10)+1):
        for num3 in range(start_number//10%10, (end_number//10%10)+1):
            for num4 in range(start_number%10, (end_number%10)+1):
                if num1 % 2 !=0 and num2 % 2 !=0 and num3 % 2 !=0 and num4 % 2 !=0:
                    print(num1,num2,num3,num4,sep='',end=' ')