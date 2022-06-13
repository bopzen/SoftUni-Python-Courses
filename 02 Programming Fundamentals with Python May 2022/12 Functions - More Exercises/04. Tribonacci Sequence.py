def tribonacci(number):
    num2 = 0
    num1 = 0
    num0 = 1
    list_trib = []
    list_trib.append(str(1))
    for i in range(number-1):
        trib_number = num0 + num1 + num2
        list_trib.append(str(trib_number))
        num2 = num1
        num1 = num0
        num0 = trib_number
    print(" ".join(list_trib))


tribonacci(int(input()))