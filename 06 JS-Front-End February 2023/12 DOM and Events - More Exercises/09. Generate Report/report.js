function generateReport() {
    let output = document.getElementById("output");
    let data = [];
    let header = Array.from(document.querySelectorAll("tr th"))
    let activeHeaders = {};
    for (let i = 0; i < header.length; i++) {
        console.log(header[i].children[0].name)
        console.log(header[i].children[0])
        if (header[i].children[0].checked) {
            activeHeaders[i] = header[i].children[0].name;
        }
    }

    let rows = Array.from(document.querySelectorAll("tbody tr"));
    
    for (const row of rows) {      
        let rowObj = {};
        let columns = Array.from(row.children);
        for (const index in activeHeaders) {
            rowObj[activeHeaders[index]] = columns[index].textContent;
        }
        data.push(rowObj)
    }
    output.textContent = JSON.stringify(data, null, 2)
}