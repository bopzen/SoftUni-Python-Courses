daljina = int(input())
shirochina = int(input())
visochina = int(input())
procent = float(input())
obem = daljina*shirochina*visochina/1000
liters = obem - obem*procent/100
print(liters)