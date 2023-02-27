function solve(array) {
    let hasLogged = false;
    let failedAttempts = 0;
    let isBlocked = false;
    let username = array[0]
    for (let index = 1; index < array.length; index++) {
        if (array[index] === username.split("").reverse().join("")) {
            hasLogged = true;
            console.log(`User ${username} logged in.`);
            break;
        } else {
            failedAttempts++;
            if (failedAttempts == 4) {
                isBlocked = true;
                console.log(`User ${username} blocked!`);
                break;
            }
            console.log('Incorrect password. Try again.')
        }
    }
}
solve (['Acer','login','go','let me in','recA']);
solve(['momo','omom']);
solve(['sunny','rainy','cloudy','sunny','not sunny']);