vacation_budget = float(input())
available_money = float(input())
days_counter = 0
consecutive_days_spend_counter = 0

while available_money < vacation_budget and consecutive_days_spend_counter <5:
    command = input()
    money = float(input())
    if command == 'spend':
        consecutive_days_spend_counter +=1
        available_money -= money
        if available_money < 0:
            available_money = 0
    elif command == 'save':
        available_money += money
        consecutive_days_spend_counter = 0
    days_counter +=1
if consecutive_days_spend_counter == 5:
    print("You can't save the money.")
    print(f"{days_counter}")
if available_money >= vacation_budget:
    print(f"You saved the money for {days_counter} days.")