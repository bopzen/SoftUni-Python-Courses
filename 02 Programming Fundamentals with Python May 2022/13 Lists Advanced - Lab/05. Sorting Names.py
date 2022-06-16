list_names = input().split(", ")
list_names.sort(key= lambda x: (-len(x),x))
print(list_names)