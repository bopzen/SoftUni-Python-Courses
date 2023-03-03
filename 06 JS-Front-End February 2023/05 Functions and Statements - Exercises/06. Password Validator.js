function checkPassword(password) {
    
    if (!isValidLength(password)) {
        console.log("Password must be between 6 and 10 characters")
    }
    if (!isValidSymbols(password)) {
        console.log("Password must consist only of letters and digits")
    }
    if (!isValidDigits(password)) {
        console.log("Password must have at least 2 digits")
    }
    if (isValidLength(password) && isValidSymbols(password) && isValidDigits(password)) {
        console.log("Password is valid")
    }
    
    function isValidLength(password) {
        if (password.length < 6 || password.length >10) {
            return false;
        }
        return true;
    }

    function isValidSymbols(password) {
        
        for (const char of password) {
            let validSymbols = (char.charCodeAt(0) >= 48 && char.charCodeAt(0) <= 57) || (char.charCodeAt(0) >= 65 && char.charCodeAt(0) <= 90) || (char.charCodeAt(0) >= 97 && char.charCodeAt(0) <= 122);
            if (!validSymbols) {
                return false;
            }
        }
        return true;
    }

    function isValidDigits(password) {
        let count = 0;        
        for (const char of password) {
            let validDigits = (char.charCodeAt(0) >= 48 && char.charCodeAt(0) <= 57);
            if (validDigits) {
                count++;
            }
            if (count ===2) {
                return true;
            }
        }
        return false;
    }
}

checkPassword('logIn');
checkPassword('MyPass123');
checkPassword('Pa$s$s');