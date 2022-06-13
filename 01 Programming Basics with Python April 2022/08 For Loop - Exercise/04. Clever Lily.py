age = int(input())
price_washing_machine = float(input())
price_toy = int(input())
money = 0
toys = 0
c = 0
for i in range(1,age+1):
    if i % 2 == 0:
        c+=1
        money+=10*c
        money-=1
    else:
        toys+=1
total = money + toys * price_toy
if total >= price_washing_machine:
    money_left = total - price_washing_machine
    print(f'Yes! {money_left:.2f}')
else:
    money_needed = price_washing_machine - total
    print(f'No! {money_needed:.2f}')