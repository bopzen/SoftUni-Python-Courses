function solve(number, ...operations) {
    for (let operation of operations) {
        switch (operation) {
            case "chop":
                number /= 2;
            break;
            case "dice":
                number = Math.sqrt(number);
            break;
            case "spice":
                number += 1;
            break;
            case "bake":
                number *= 3;
            break;
            case "fillet":
                number = number - number * 0.2;
            break;
        }
        console.log(number);
    }
}
solve('32', 'chop', 'chop', 'chop', 'chop', 'chop');