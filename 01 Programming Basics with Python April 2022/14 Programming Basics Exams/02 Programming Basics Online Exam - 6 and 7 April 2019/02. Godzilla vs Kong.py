budget = float(input())
statists = int(input())
costume_price = float(input())
decor = budget * 0.1
cost_statists = statists * costume_price
if statists >150:
    cost_statists -= cost_statists*0.1
total_cost = decor + cost_statists
diff = budget - total_cost
if total_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {abs(diff):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(diff):.2f} leva left.")
