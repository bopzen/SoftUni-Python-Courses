function colorize() {
    let evenRows = document.querySelectorAll("tr:nth-child(even)");
    for (const row of evenRows) {
        row.style.background = "Teal";
    }
}