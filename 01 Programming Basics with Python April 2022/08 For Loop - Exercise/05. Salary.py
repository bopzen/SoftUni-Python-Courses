count_tabs = int(input())
salary = float(input())
for i in range(count_tabs):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50
    if salary <=0:
        print("You have lost your salary.")
        break
if salary >0:
    print(int(salary))