trip_price = float(input())
count_puzzle = int(input())
count_doll = int(input())
count_bear = int(input())
count_minion = int(input())
count_truck = int(input())
profit = count_puzzle*2.6 + count_doll*3 + count_bear*4.1 + count_minion*8.2 + count_truck*2
count_all = count_truck + count_bear + count_doll + count_minion + count_puzzle
if count_all>=50:
    profit-=profit*0.25
net_profit = profit - profit*0.1
if trip_price <= net_profit:
    money_remaining = net_profit - trip_price
    print(f'Yes! {money_remaining:.2f} lv left.')
else:
    money_needed = trip_price - net_profit
    print(f'Not enough money! {money_needed:.2f} lv needed.')