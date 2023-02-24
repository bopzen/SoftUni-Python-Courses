function solve(text) {
    let textArray = text.split(/(?=[A-Z])/);
    console.log(textArray.join(", "));
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan');