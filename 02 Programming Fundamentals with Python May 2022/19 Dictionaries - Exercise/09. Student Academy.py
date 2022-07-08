students_dict = {}
n = int(input())
for i in range(n):
    name = input()
    grade = float(input())
    if name not in students_dict:
        students_dict[name] = [grade]
    else:
        students_dict[name].append(grade)

print("\n".join(f"{key} -> {sum(students_dict[key])/len(students_dict[key]):.2f}" for key in students_dict.keys() if sum(students_dict[key])/len(students_dict[key]) >= 4.5))
