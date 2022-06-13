price_skumria = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = float(input())

amount = kg_palamud * price_skumria * 1.6 + kg_safrid * price_caca * 1.8 + kg_midi * 7.5
print('{:.2f}'.format(amount))