company = input()
count_tickets_adults = int(input())
count_tickets_kids = int(input())
price_adults = float(input())
price_service = float(input())
profit = count_tickets_adults*(price_adults + price_service) + count_tickets_kids*((price_adults-price_adults*0.7)+price_service)
net_profit = profit*0.2
print(f'The profit of your agency from {company} tickets is {net_profit:.2f} lv.')