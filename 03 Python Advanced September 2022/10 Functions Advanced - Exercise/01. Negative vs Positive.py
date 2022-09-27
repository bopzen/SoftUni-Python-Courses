def calculate_sum(*args):
    sum_positive = 0
    sum_negative = 0
    for num in args:
        if num > 0:
            sum_positive += num
        else:
            sum_negative += num
    return sum_positive, sum_negative


entry = [int(x) for x in input().split()]

result = calculate_sum(*entry)
print(result[1])
print(result[0])

if abs(result[0]) > abs(result[1]):
    print("The positives are stronger than the negatives")
else:
    print("The negatives are stronger than the positives")