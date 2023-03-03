function printDNA(length) {
    let sequence = "ATCGTTAGGG";
    let asterix = 2;
    let hyphen = 0;
    let sequenceCounter = 0;
    let counter = 0;
    for (let i = 1; i <= length; i++) {
        if (sequenceCounter == 10) {
            sequenceCounter = 0;
        }
        let row = "*".repeat(asterix) + sequence[sequenceCounter] + "-".repeat(hyphen*2) + sequence[sequenceCounter + 1] + "*".repeat(asterix);
        console.log(row);
        sequenceCounter += 2;
        if (counter == 2) {
            counter = -2;
        }
        if (counter >= 0) {
            asterix--;
            hyphen++;
        } else {
            asterix++;
            hyphen--;
        }
        counter++       
    }
}

printDNA(4);
printDNA(10);