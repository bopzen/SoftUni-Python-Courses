function solve(input) {
    let garage = {};
    for (const line of input) {
        let [garageNumber, restLine] = line.split(" - ");
            if (!garage.hasOwnProperty(garageNumber)) {
                garage[garageNumber] = [];
            }
        let tokens = restLine.split(", ");
        let car = {};
        for (const token of tokens) {
            let tokenSplit = token.split(": ");     
            for (let i = 0; i < tokenSplit.length; i+=2) {
                car[tokenSplit[i]] = tokenSplit[i + 1];     
            }           
        }
        garage[garageNumber].push(car);
    }
    for (const key in garage) {
        console.log(`Garage № ${key}`);
        for (const car of garage[key]) {
            let carString = [];
            let carEntries = Object.entries(car);
            for (const [key,value] of carEntries) {
                carString.push(`${key} - ${value}`)
            }    
            console.log(`--- ${carString.join(", ")}`);     
        }     
    }
}

solve(['1 - color: blue, fuel type: diesel', '1 - color: red, manufacture: Audi', '2 - fuel type: petrol', '4 - color: dark blue, fuel type: diesel, manufacture: Fiat']);
solve(['1 - color: green, fuel type: petrol',
'1 - color: dark red, manufacture: WV',
'2 - fuel type: diesel',
'3 - color: dark blue, fuel type: petrol']
);