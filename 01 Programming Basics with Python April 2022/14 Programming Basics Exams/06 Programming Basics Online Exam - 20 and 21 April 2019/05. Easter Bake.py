import math,sys
count_kozunak = int(input())
total_sugar_gr = 0
total_flour_gr = 0
max_sugar_gr = -sys.maxsize
max_flour_gr = -sys.maxsize

for i in range(count_kozunak):
    sugar_gr = int(input())
    flour_gr = int(input())
    total_sugar_gr += sugar_gr
    total_flour_gr += flour_gr
    if sugar_gr > max_sugar_gr:
        max_sugar_gr = sugar_gr
    if flour_gr > max_flour_gr:
        max_flour_gr = flour_gr

total_sugar_packs = math.ceil(total_sugar_gr/950)
total_flour_packs = math.ceil(total_flour_gr/750)

print(f"Sugar: {total_sugar_packs}")
print(f"Flour: {total_flour_packs}")
print(f"Max used flour is {max_flour_gr} grams, max used sugar is {max_sugar_gr} grams.")
