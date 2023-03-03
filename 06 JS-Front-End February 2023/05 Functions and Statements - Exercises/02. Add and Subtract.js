function solve(numberOne, numberTwo, numberThree) {
    function sum(numOne, numTwo) {
        return numOne + numTwo;
    }
    function subtract(numOne, numTwo, numThree) {
        return sum(numOne, numTwo) - numThree
    }
    return subtract(numberOne, numberTwo, numberThree);
}

console.log(solve(23, 6, 10));
