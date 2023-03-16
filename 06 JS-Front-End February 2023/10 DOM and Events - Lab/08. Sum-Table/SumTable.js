function sumTable() {
    let products = document.querySelectorAll("td:nth-child(even):not(#sum)");
    let total = 0;
    for (const product of products) {
        total += Number(product.textContent);
    }
    let result = document.getElementById("sum");
    result.textContent = total;
}