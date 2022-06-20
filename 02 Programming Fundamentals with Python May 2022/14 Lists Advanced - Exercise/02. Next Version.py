list_version = list(map(int, input().split(".")))
for index in range(len(list_version) - 1, -1, -1):
    if list_version[index] < 9:
        list_version[index] += 1
        break
    else:
        list_version[index] = 0
        continue
print(".".join(map(str, list_version)))