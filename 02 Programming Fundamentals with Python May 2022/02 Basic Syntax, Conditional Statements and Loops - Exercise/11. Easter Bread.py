budget = float(input())
price_1kg_flour = float(input())
price_1pack_eggs = price_1kg_flour * 0.75
price_250ml_milk = (price_1kg_flour + price_1kg_flour * 0.25) / 4
price_loaf = price_1kg_flour + price_1pack_eggs + price_250ml_milk
count_loaves = 0
count_eggs = 0

while budget >= price_loaf:
    count_loaves +=1
    count_eggs +=3
    if count_loaves % 3 == 0:
        count_eggs -= count_loaves - 2
    budget -= price_loaf
print(f"You made {count_loaves} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")