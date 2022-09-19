lines = int(input())
longest_intersection = set()
for _ in range(lines):
    set1 = set()
    set2 = set()
    range1, range2 = input().split("-")
    start_index1, end_index1 = tuple(map(int, range1.split(",")))
    start_index2, end_index2 = tuple(map(int, range2.split(",")))
    for i in range(start_index1, end_index1 + 1):
        set1.add(i)
    for i in range(start_index2, end_index2 +1):
        set2.add(i)
    current_intersection = set1.intersection(set2)
    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection
print(f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length {len(longest_intersection)}")