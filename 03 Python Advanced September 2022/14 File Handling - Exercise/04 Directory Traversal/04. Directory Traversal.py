import os

files_dict = {}
directory = 'Files'

for filename_zero_level in os.listdir(directory):
    file_zero_level = os.path.join(directory, filename_zero_level)
    if os.path.isfile(file_zero_level):
        file = file_zero_level.split('\\')[-1]
        extension = file.split('.')[1]
        if extension not in files_dict:
            files_dict[extension] = []
            files_dict[extension].append(file)
        else:
            files_dict[extension].append(file)
    else:
        for filename_first_level in os.listdir(file_zero_level):
            file_first_level = os.path.join(file_zero_level, filename_first_level)
            if os.path.isfile(file_first_level):
                file = file_first_level.split('\\')[-1]
                extension = file.split('.')[1]
                if extension not in files_dict:
                    files_dict[extension] = []
                    files_dict[extension].append(file)
                else:
                    files_dict[extension].append(file)
files_dict_sorted = sorted(files_dict.items(), key=lambda x: x[0])

with open(f'{directory}\\report.txt', 'w') as report_file:
    for extension, files in files_dict_sorted:
        report_file.write(f'{extension}\n')
        for file in sorted(files):
            report_file.write(f'- - - {file}\n')