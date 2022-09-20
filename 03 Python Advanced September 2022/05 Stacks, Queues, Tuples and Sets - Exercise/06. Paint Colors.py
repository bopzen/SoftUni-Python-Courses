from collections import deque

string_colors = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

found_colors = []
final_colors = []

while string_colors:
    if len(string_colors) == 1:
        if string_colors[0]:
            if string_colors[0] in main_colors or string_colors[0] in secondary_colors:
                found_colors.append(string_colors[0])
            string_colors[0] = string_colors[0][:-1]
        else:
            break
    else:
        first_substring = string_colors.popleft()
        last_substring = string_colors.pop()
        check_color1 = first_substring + last_substring
        check_color2 = last_substring + first_substring
        if check_color1 in main_colors or check_color1 in secondary_colors:
            found_colors.append(check_color1)
        elif check_color2 in main_colors or check_color2 in secondary_colors:
            found_colors.append(check_color2)
        else:
            first_substring = first_substring[:-1]
            last_substring = last_substring[:-1]
            if first_substring:
                string_colors.insert(len(string_colors) // 2, first_substring)
            if last_substring:
                string_colors.insert(len(string_colors) // 2, last_substring)

for element in found_colors:
    if element == 'orange':
        if 'red' in found_colors and 'yellow' in found_colors:
            final_colors.append(element)
    elif element == 'purple':
        if 'red' in found_colors and 'blue' in found_colors:
            final_colors.append(element)
    elif element == 'green':
        if 'yellow' in found_colors and 'blue' in found_colors:
            final_colors.append(element)
    else:
        final_colors.append(element)
print(final_colors)