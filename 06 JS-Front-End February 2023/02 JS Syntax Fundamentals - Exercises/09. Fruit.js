function solve(name, grams, price) {
    let kg = grams / 1000;
    let total = price * kg;
    console.log(`I need $${total.toFixed(2)} to buy ${kg.toFixed(2)} kilograms ${name}.`);
}

solve('orange', 2500, 1.80);