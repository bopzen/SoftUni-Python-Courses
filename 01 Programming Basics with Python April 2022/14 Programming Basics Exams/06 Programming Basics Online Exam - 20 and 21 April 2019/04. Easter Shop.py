initial_amount_eggs = int(input())
left_eggs = initial_amount_eggs
sold_eggs = 0
while True:
    command = input()
    if command == 'Close':
        print("Store is closed!")
        print(f"{sold_eggs} eggs sold.")
        break
    amount_eggs = int(input())
    if command == 'Buy':
        if amount_eggs > left_eggs:
            print("Not enough eggs in store!")
            print(f"You can buy only {left_eggs}.")
            break
        else:
            left_eggs -= amount_eggs
            sold_eggs += amount_eggs
    elif command == 'Fill':
        left_eggs += amount_eggs
