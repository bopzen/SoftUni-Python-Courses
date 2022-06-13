list_integers_str = input().split(", ")
list_integers = []
list_integers_new = []
count_zeroes = 0
for element in list_integers_str:
    list_integers.append(int(element))
for element in list_integers:
    if element == 0:
        count_zeroes += 1
    else:
        list_integers_new.append(element)
for i in range(count_zeroes):
    list_integers_new.append(0)
print(list_integers_new)