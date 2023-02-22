function solve(text, searchedWord) {
    let textArray = text.split(" ");
    let counter = 0;
    for (let word of textArray) {
        if (word === searchedWord) {
            counter++;
        }
    }
    console.log(counter);
}

solve('This is a word and it also is a sentence','is');