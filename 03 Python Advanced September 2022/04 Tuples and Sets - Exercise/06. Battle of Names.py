lines = int(input())
set_odd = set()
set_even = set()
for row in range(1, lines+1):
    name = input()
    value = 0
    for ch in name:
        value += ord(ch)
    value //= row
    if value % 2 == 0:
        set_even.add(value)
    else:
        set_odd.add(value)
sum_set_odd = sum(set_odd)
sum_set_even = sum(set_even)
if sum_set_even ==  sum_set_odd:
    print(", ".join(str(x) for x in set_odd | set_even))
elif sum_set_odd > sum_set_even:
    print(", ".join(str(x) for x in set_odd - set_even))
else:
    print(", ".join(str(x) for x in set_odd ^ set_even))