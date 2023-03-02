function calculatePrice(product, quantity) {
    let prices = {
        "coffee": 1.50, 
        "water": 1.00, 
        "coke": 1.40, 
        "snacks": 2.00
    }
    let result = quantity * prices[product];
    return result.toFixed(2);
}

console.log(calculatePrice("water", 5));
