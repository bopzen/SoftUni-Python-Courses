annual_fee = int(input())
sneakers = annual_fee - annual_fee *0.4
kit = sneakers - sneakers *0.2
ball = kit /4
accessories = ball /5
total = annual_fee + sneakers + kit + ball + accessories
print(f'{total:.2f}')