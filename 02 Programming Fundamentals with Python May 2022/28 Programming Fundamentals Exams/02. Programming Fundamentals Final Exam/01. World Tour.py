stops = input()
while True:
    command = input()
    if command == 'Travel':
        break
    tokens = command.split(":")
    action = tokens[0]
    if action == 'Add Stop':
        index, string = int(tokens[1]), tokens[2]
        if 0 <= index < len(stops):
            stops = stops[:index] + string + stops[index:]

    elif action == 'Remove Stop':
        start_index, end_index = int(tokens[1]), int(tokens[2])
        if 0 <= start_index <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+1:]

    elif action == 'Switch':
        old_string, new_string = tokens[1], tokens[2]
        stops = stops.replace(old_string, new_string)
    print(stops)
print(f"Ready for world tour! Planned stops: {stops}")
