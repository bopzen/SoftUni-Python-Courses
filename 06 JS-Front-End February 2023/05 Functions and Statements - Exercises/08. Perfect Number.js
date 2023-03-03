function checkPerfectNumber(number) {
    let divisorsSum = 0;
    for (let index = 1; index < number; index++) {
        if (number % index === 0) {
            divisorsSum += index
        }     
    }
    if (divisorsSum === number) {
        console.log("We have a perfect number!");
    } else {
        console.log("It's not so perfect.")
    }
}

checkPerfectNumber(6);
