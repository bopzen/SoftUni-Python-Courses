def find_smallest(a, b, c):
    min_number = None
    if a < b and a < c:
        min_number = a
    elif b < a and b < c:
        min_number = b
    elif c < a and c < b:
        min_number = c
    return min_number


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(find_smallest(first_number, second_number, third_number))