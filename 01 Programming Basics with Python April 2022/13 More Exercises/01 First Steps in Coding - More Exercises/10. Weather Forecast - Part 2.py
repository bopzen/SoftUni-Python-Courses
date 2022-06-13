degrees = float(input())
if degrees >=5 and degrees <=11.9:
    print("Cold")
elif degrees >=12 and degrees <=14.9:
    print("Cool")
elif degrees >=15 and degrees <=20:
    print("Mild")
elif degrees >=20.1 and degrees <=25.9 :
    print("Warm")
elif degrees >=26 and degrees <=35:
    print("Hot")
else:
    print("unknown")