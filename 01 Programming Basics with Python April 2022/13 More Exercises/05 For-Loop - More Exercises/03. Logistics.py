count_shipments = int(input())
price = 0
p_bus = 0
p_truck = 0
p_train = 0
shipment_bus = 0
shipment_truck = 0
shipment_train = 0
for i in range(count_shipments):
    shipment = int(input())
    if shipment <= 3:
        shipment_bus+= shipment
    elif shipment <= 11:
        shipment_truck += shipment
    else:
        shipment_train += shipment
total_shipment = shipment_bus + shipment_truck + shipment_train
total_price = shipment_bus * 200 + shipment_truck * 175 + shipment_train * 120
average_price = total_price/total_shipment
perc_bus = shipment_bus / total_shipment * 100
perc_truck = shipment_truck / total_shipment * 100
perc_train = shipment_train / total_shipment * 100
print(f'{average_price:.2f}')
print(f'{perc_bus:.2f}%')
print(f'{perc_truck:.2f}%')
print(f'{perc_train:.2f}%')