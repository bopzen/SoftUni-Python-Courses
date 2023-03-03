function factorialDivision(numOne, numTwo) {
    return `${(factorial(numOne) / factorial(numTwo)).toFixed(2)}`;

    function factorial(number) {
        if (number === 1) {
            return number;
        }
        return number * factorial(number - 1);
    }
}

console.log(factorialDivision(5, 2));