company_dict = {}

while True:
    command = input()
    if command == 'End':
        break
    list_command = command.split(" -> ")
    company_name, employee_id = list_command[0], list_command[1]
    if company_name not in company_dict:
        company_dict[company_name] = [employee_id]
    else:
        if employee_id not in company_dict[company_name]:
            company_dict[company_name].append(employee_id)

for key, value in company_dict.items():
    print(f"{key}")
    for element in value:
        print(f"-- {element}")