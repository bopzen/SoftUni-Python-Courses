function solve(text) {
    let textArray = text.split(" ");
    for (let word of textArray) {
        if (word.startsWith("#") && word.length > 1) {
            let checkWord = word.slice(1);
            let isValid = true;
            for (const symbol of checkWord) {
                let asciiCode = symbol.toLowerCase().charCodeAt(0)
                if (!(asciiCode >= 97 && asciiCode <= 122)) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                console.log(checkWord);
            }
        }
    }
}

solve('Nowadays everyone uses # to tag a #special word in #socialMedia');
solve('The symbol # is known #variously in English-speaking #regions as the #number sign');