n = int(input())
for _ in range(n):
    text = input()
    name = ""
    age = ""
    copy_name = False
    copy_age = False
    for ch in text:
        if ch == "@":
            copy_name = True
            continue
        if ch == "|":
            copy_name = False
            continue
        if ch == "#":
            copy_age = True
            continue
        if ch == "*":
            copy_age = False
            continue

        if copy_name:
            name += ch
        if copy_age:
            age += ch
    print(f"{name} is {age} years old.")

