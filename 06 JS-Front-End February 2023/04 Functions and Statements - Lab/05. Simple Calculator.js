function simpleCalculator(numOne, numTwo, operator) {
    const add = (a, b) => a + b;
    const subtract = (a, b) => a - b;
    const multiply = (a, b) => a * b;
    const divide = (a, b) => a / b;
    const operations = {
        add: add,
        subtract: subtract,
        multiply: multiply,
        divide: divide
    }
    return operations[operator](numOne, numTwo);
}

console.log(simpleCalculator(5,
    5,
    'multiply'
    ));
