function printMatrix(number) {
    for (let index = 0; index < number; index++) {
        console.log((number.toString() + " ").repeat(number));     
    }
}

printMatrix(5);