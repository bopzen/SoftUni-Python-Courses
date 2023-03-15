function solve(input) {
    let products = {};
    for (const line of input) {
        let [name, price] = line.split(" : ");
        if (!products.hasOwnProperty(name[0])) {
            products[name[0]] = {}
        }
        products[name[0]][name] = Number(price);
    }
    let sortedKeys = Object.keys(products).sort((a, b) => a.localeCompare(b));
    for (const key of sortedKeys) {
        console.log(key);
        let sortedProducts = Object.entries(products[key]).sort((a, b) => a[0].localeCompare(b[0]));
        for (const [key, value] of sortedProducts) {
            console.log(`  ${key}: ${value}`)
        }
    }
}

solve([
    'Appricot : 20.4',
    'Fridge : 1500',
    'TV : 1499',
    'Deodorant : 10',
    'Boiler : 300',
    'Apple : 1.25',
    'Anti-Bug Spray : 15',
    'T-Shirt : 10'
    ]
    );
solve([
    'Omlet : 5.4',
    'Shirt : 15',
    'Cake : 59'
    ]
    );