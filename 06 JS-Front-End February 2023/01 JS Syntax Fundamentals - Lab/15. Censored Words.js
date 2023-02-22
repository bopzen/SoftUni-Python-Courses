function solve(text, bannedWord) {
    let censoredText = text;
    while (censoredText.includes(bannedWord)) {
        censoredText = censoredText.replace(bannedWord, "*".repeat(bannedWord.length))
    }
    console.log(censoredText);
}

solve('A small sentence with some words',

'small');