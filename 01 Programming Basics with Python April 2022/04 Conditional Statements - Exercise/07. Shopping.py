budget = float(input())
count_gpu = int(input())
count_cpu = int(input())
count_ram = int(input())
gpu_total_price = count_gpu * 250
cpu_price = gpu_total_price * 0.35
ram_price = gpu_total_price * 0.10

cpu_total_price = cpu_price * count_cpu
ram_total_price = ram_price * count_ram

total_price = gpu_total_price + cpu_total_price + ram_total_price
if count_gpu > count_cpu:
    discount = 0.15 * total_price
    total_price -=discount
if budget>=total_price:
    money_left = budget - total_price
    print(f'You have {money_left:.2f} leva left!')
else:
    money_more_needed = total_price - budget
    print(f'Not enough money! You need {money_more_needed:.2f} leva more!')