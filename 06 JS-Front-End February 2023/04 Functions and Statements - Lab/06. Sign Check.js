function signCheck(numOne, numTwo, numThree) {
    let countNegative = [numOne, numTwo, numThree].filter((x) => x < 0).length;
    return countNegative % 2 === 0 ? "Positive" : "Negative"
}

console.log(signCheck( 5,
    12,
   -15
   ));