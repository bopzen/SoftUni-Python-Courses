dwarf_stats = {}
colors = {}
while True:
    command = input()
    if command == 'Once upon a time':
        break
    list_command = command.split(" <:> ")
    dwarf_name, dwarf_hat_color, dwarf_physics = list_command[0], list_command[1], int(list_command[2])
    dwarf_id = dwarf_name + ":" + dwarf_hat_color
    if dwarf_id not in dwarf_stats:
        dwarf_stats[dwarf_id] = [dwarf_physics, dwarf_hat_color]
        if dwarf_hat_color not in colors:
            colors[dwarf_hat_color] = 1
        else:
            colors[dwarf_hat_color] += 1
    else:
        if dwarf_physics > dwarf_stats[dwarf_id][0]:
            dwarf_stats[dwarf_id] = [dwarf_physics, dwarf_hat_color]

sorted_dwarf = dict(sorted(dwarf_stats.items(),key=lambda x:(-x[1][0], -colors[x[1][1]])))

for key, value in sorted_dwarf.items():
    tokens = key.split(":")
    print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")