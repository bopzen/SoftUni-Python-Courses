function printRange(charOne, charTwo) {
    let start = Math.min(charOne.charCodeAt(0), charTwo.charCodeAt(0));
    let end = Math.max(charOne.charCodeAt(0), charTwo.charCodeAt(0));
    let charsArray = [];
    for (let index = start + 1; index < end; index++) {
        charsArray.push(String.fromCharCode(index))       
    }
    console.log(charsArray.join(" "));
}

printRange("A", "Z");