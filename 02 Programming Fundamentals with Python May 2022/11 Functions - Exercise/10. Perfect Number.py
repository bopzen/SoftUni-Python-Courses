def perfect_number(number):
    sum_amount = 0
    for i in range(1, number):
        if number % i == 0:
            sum_amount += i
    if sum_amount == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


perfect_number(int(input()))