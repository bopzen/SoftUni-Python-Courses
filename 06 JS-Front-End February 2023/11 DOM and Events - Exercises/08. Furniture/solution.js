function solve() {
  let [input, output] = document.getElementsByTagName("textarea");
  let [generateBtn, buyBtn] = document.getElementsByTagName("button");
  let table = document.getElementsByTagName("tbody")[0];
  generateBtn.addEventListener("click", generateHandler);
  
  function generateHandler() {
    let inputData = JSON.parse(input.value);
    for (const entry of inputData) {
      console.log(entry);
      let tr = document.createElement("tr");

      let tdImage = document.createElement("td");
      let img = document.createElement("img");
      img.setAttribute("src", entry.img);
      tdImage.appendChild(img);
      tr.appendChild(tdImage);

      let tdName = document.createElement("td");
      let tdNameP = document.createElement("p");
      tdNameP.textContent = entry.name;
      tdName.appendChild(tdNameP);
      tr.appendChild(tdName);

      let tdPrice = document.createElement("td");
      let tdPriceP = document.createElement("p");
      tdPriceP.textContent = entry.price;
      tdPrice.appendChild(tdPriceP);
      tr.appendChild(tdPrice);

      let tdDecFactor = document.createElement("td");
      let tdDecFactorP = document.createElement("p");
      tdDecFactorP.textContent = entry.decFactor;
      tdDecFactor.appendChild(tdDecFactorP);
      tr.appendChild(tdDecFactor);

      let tdMark = document.createElement("td");
      let input = document.createElement("input");
      input.setAttribute("type", "checkbox");
      tdMark.appendChild(input);
      tr.appendChild(tdMark);

      table.appendChild(tr);
    }
  }

  buyBtn.addEventListener("click", buyHandler);

  function buyHandler() {
    let boughtProducts = [];
    let totalPrice = 0;
    let totalFactor = 0;
    let allChecked = document.querySelectorAll("tbody tr td input:checked");
    for (const input of allChecked) {
      let tableRow = input.parentElement.parentElement;
      let [image, name, price, decFactor, mark] = Array.from(tableRow.children);
      let item = name.children[0].textContent;
      let itemPrice = price.children[0].textContent;
      let itemFactor = decFactor.children[0].textContent;
      boughtProducts.push(item);
      totalPrice += Number(itemPrice);
      totalFactor += Number(itemFactor);
    }
    let avgFactor = totalFactor / boughtProducts.length;
    output.value = `Bought furniture: ${boughtProducts.join(", ")}\nTotal price: ${totalPrice.toFixed(2)}\nAverage decoration factor: ${avgFactor}`
  }
}