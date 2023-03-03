function loadBar(progress) {
    if (progress < 100) {
        console.log(`${progress}% ` + printBar(progress));
        console.log("Still loading...");
    } else {
        console.log(`${progress}% Complete!`);
        console.log(printBar(progress));
    }

    function printBar(progress) {
        let result = "";
        result += "[" + "%".repeat(progress/10) + ".".repeat(10 - progress/10) + "]";
        return result;
    }
}

loadBar(30);
loadBar(60);
loadBar(100);