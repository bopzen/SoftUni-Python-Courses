men = int(input())
women = int(input())
max_tables = int(input())
tables = 0
is_full = False
for m in range(1, men+1):
    for f in range(1, women+1):
        tables += 1
        print(f"({m} <-> {f})", end=' ')
        if tables == max_tables:
            is_full = True
            break
    if is_full:
        break