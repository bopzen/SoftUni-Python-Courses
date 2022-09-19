n, m = tuple(map(int,input().split()))
set1 = set()
set2 = set()
for _ in range(n):
    set1.add(int(int(input())))
for _ in range(m):
    set2.add(int(int(input())))

intersection_set = set1.intersection(set2)
for num in intersection_set:
    print(num)