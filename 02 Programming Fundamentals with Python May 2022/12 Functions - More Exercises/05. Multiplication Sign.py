num1 = int(input())
num2 = int(input())
num3 = int(input())

list_num = [num1, num2, num3]
count_zero = len(list(filter(lambda x: x ==0,list_num)))
count_negative = len(list(filter(lambda x: x < 0,list_num)))
if count_zero >= 1:
    print('zero')
elif count_negative >=1:
    if count_negative % 2 == 0:
        print('positive')
    else:
        print('negative')
else:
    print('positive')