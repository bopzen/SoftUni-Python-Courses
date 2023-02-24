function solve(words, text) {
    let wordsList = words.split(", ");
    for (let word of wordsList) {
        let wordLength = word.length;
        let replaceAsterix = "*".repeat(wordLength)
        text = text.replace(replaceAsterix, word)
    }
    console.log(text);
}

solve('great',
'softuni is ***** place for learning new programming languages'
);