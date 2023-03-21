function solve() {
    let table = document.getElementsByTagName("table")[0];
    let result = document.querySelector("#check p");
    let inputs = Array.from(document.querySelectorAll("input"));
    let [checkBtn, clearBtn] = document.getElementsByTagName("button");
    checkBtn.addEventListener("click", checkBtnHandler);
    clearBtn.addEventListener("click", clearBtnHandler);

    function checkBtnHandler() {
        let matrix = [
            [inputs[0].value, inputs[1].value, inputs[2].value],
            [inputs[3].value, inputs[4].value, inputs[5].value],
            [inputs[6].value, inputs[7].value, inputs[8].value]
        ];
        isSudomu = true;
        for (let i = 1; i < matrix.length; i++) {
            let row = matrix[i];
            let col = matrix.map(row => row[i]);
            if (col.length != [...new Set(col)].length || row.length != [...new Set(row)].length) {
                isSudomu = false;
                break;
            }
        }
        if (isSudomu) {
            table.style.border = '2px solid green';
            result.style.color = 'green';
            result.textContent = 'You solve it! Congratulations!';
        } else {
            table.style.border = '2px solid red';
            result.style.color = 'red';
            result.textContent = 'NOP! You are not done yet...';
        }
    }

    function clearBtnHandler() {
        table.style.border = "none";
        result.textContent = "";
        for (const input of inputs) {
            input.value = "";
        }
    }
}