function deleteByEmail() {
    let result = document.getElementById("result");
    let email = document.getElementsByName("email")[0].value;
    let secondColumn = document.querySelectorAll("#customers tr td:nth-child(even)");
    for (const td of secondColumn) {
        if (td.textContent === email) {
            td.parentNode.remove();
            result.textContent = "Deleted.";
            return;
        }
    }
    result.textContent = "Not found." 
}