function solve(checkWord, text) {
    let textArr = text.split(" ");
    let isFound = false;
    for (const word of textArr) {
        if (word.toLowerCase() === checkWord) {
            console.log(checkWord);
            isFound = true;
            break;
        }
    }
    if (!isFound) {
        console.log(`${checkWord} not found!`)
    }
}

solve('javascript','JavaScript is the best programming language');
solve('python','JavaScript is the best programming language');