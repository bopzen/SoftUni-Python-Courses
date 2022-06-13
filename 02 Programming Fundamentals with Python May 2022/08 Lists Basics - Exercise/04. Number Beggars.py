list_numbers = input().split(", ")
count_beggars = int(input())
list_sum_beggars = []
for i in range(1, count_beggars+1):
    current_sum = 0
    for index in range(i-1,len(list_numbers),count_beggars):
        current_sum += int(list_numbers[index])
    list_sum_beggars.append(current_sum)
print(list_sum_beggars)