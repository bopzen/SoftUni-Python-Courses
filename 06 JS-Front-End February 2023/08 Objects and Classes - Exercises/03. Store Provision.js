function solve(stock, ordered) {
    let storeStock = {};
    for (let i = 0; i < stock.length; i+=2) {
        storeStock[stock[i]] = Number(stock[i + 1]);
    }
    for (let i = 0; i < ordered.length; i+=2) {
        if (storeStock.hasOwnProperty(ordered[i])) {
            storeStock[ordered[i]] += Number(ordered[i + 1]);
        } else {
            storeStock[ordered[i]] = Number(ordered[i + 1]);
        }
    }
    for (const product in storeStock) {
        console.log(`${product} -> ${storeStock[product]}`);
    }
}

solve([
    'Chips', '5', 'CocaCola', '9', 'Bananas', '14', 'Pasta', '4', 'Beer', '2'
    ],
    [
    'Flour', '44', 'Oil', '12', 'Pasta', '7', 'Tomatoes', '70', 'Bananas', '30'
    ]
);

solve([
    'Salt', '2', 'Fanta', '4', 'Apple', '14', 'Water', '4', 'Juice', '5'
    ],
    [
    'Sugar', '44', 'Oil', '12', 'Apple', '7', 'Tomatoes', '7', 'Bananas', '30'
    ]
);