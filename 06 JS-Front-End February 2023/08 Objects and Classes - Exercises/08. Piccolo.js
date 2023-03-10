function solve(input) {
    let parkingLot = [];
    for (const line of input) {
        let [direction, carNumber] = line.split(", ");
        if (direction === "IN") {
            if (!parkingLot.includes(carNumber)) {
                parkingLot.push(carNumber);
            }            
        } else if (direction === "OUT") {
            if (parkingLot.includes(carNumber)) {
                parkingLot.splice(parkingLot.indexOf(carNumber), 1);
            }     
        }
    }
    if (parkingLot.length > 0) {
        console.log(parkingLot.sort().join("\n"));
    } else {
        console.log("Parking Lot is Empty")
    }
}

solve(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'IN, CA9999TT',
'IN, CA2866HI',
'OUT, CA1234TA',
'IN, CA2844AA',
'OUT, CA2866HI',
'IN, CA9876HH',
'IN, CA2822UU']
);

solve(['IN, CA2844AA',
'IN, CA1234TA',
'OUT, CA2844AA',
'OUT, CA1234TA']
);