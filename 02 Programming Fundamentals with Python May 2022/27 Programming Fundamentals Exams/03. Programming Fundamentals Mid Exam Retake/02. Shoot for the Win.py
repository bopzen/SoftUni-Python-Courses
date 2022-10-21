list_targets = list(map(int,input().split()))

while True:
    command = input()
    if command == 'End':
        break
    index = int(command)
    if 0 <= index < len(list_targets):
        current_target = list_targets[index]
        list_targets[index] = -1
        for i in range(len(list_targets)):
            if list_targets[i] != -1:
                if list_targets[i] > current_target:
                    list_targets[i] -= current_target
                else:
                    list_targets[i] += current_target
    else:
        continue
count_shots = list_targets.count(-1)
targets_str = list(map(str,list_targets))
targets = " ".join(targets_str)
print(f"Shot targets: {count_shots} -> {targets}")