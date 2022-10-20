bitcoins = int(input())
yuans = float(input())
commission = float(input())
total_eur = bitcoins*1168/1.95+yuans*0.15*1.76/1.95
total_eur-=total_eur*commission/100
print(f'{total_eur:.2f}')