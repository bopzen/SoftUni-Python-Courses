import math
price_racket = float(input())
count_racket = int(input())
count_sneakers = int(input())
price_sneakers = price_racket / 6
price_racket_sneakers = count_racket *price_racket + count_sneakers *price_sneakers
price_equipment = price_racket_sneakers* 0.2
total_price = price_racket_sneakers + price_equipment
paid_by_djokovic = math.floor(total_price / 8)
paid_by_sponsor = math.ceil(total_price * 7/8)
print(f"Price to be paid by Djokovic {paid_by_djokovic}")
print(f"Price to be paid by sponsors {paid_by_sponsor}")