list_numbers = input().split()
k = int(input())
list_execution = []
index = 0
while len(list_numbers) > 1:
    for i in range(k-1):
        index +=1
        if index > len(list_numbers)-1:
            diff = index - len(list_numbers)
            index = 0 + diff
    executed = list_numbers[index]
    list_numbers.pop(index)
    list_execution.append(executed)
list_execution.append(list_numbers[0])
print('[', end='')
for i in range(len(list_execution)-1):
    print(f'{list_execution[i]},', end='')
print(f'{list_execution[-1]}', end='')
print(']', end='')