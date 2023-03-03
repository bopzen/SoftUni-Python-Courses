function checkPalindrome(array) {
    let result = []
    for (const number of array) {
        if (number.toString().split("").toString() === number.toString().split("").reverse().toString()) {
            console.log(true);
        } else {
            console.log(false);
        }
    }
}

checkPalindrome([123,323,421,121]);