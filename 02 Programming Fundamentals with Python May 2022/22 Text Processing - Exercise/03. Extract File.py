path = input()
split_path = path.split("\\")
full_file_name = split_path[-1]
file_name, file_extension = full_file_name.split(".")
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")