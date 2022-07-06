list_letters = input().split(", ")
ascii_dict = {element:ord(element) for element in list_letters}
print(ascii_dict)