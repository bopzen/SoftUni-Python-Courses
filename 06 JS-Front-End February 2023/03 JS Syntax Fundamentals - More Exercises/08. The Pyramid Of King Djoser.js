function solve(base, increment) {
    let stone = 0;
    let marble = 0;
    let lapisLazuli = 0;
    let gold = 0;
    let steps = 1;
    while (base > 2) {
        stone += (base - 2) * (base - 2) * increment;
        if (steps % 5 == 0) {
            lapisLazuli += (base * base - (base - 2) * (base - 2)) * increment;
        } else {
            marble += ((base - 2) * 4 + 4) * increment;
        }
        base -= 2;
        steps++
    }
    gold += base * base * increment;
    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapisLazuli)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${Math.floor(steps * increment)}`);
}


solve(12, 1);
solve(23, 0.5);
solve(11, 1);
solve(11, 0.75);