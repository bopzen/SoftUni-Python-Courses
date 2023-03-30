const BASE_URL = "http://localhost:3030/jsonstore/grocery/";
let product = document.getElementById("product");
let count = document.getElementById("count");
let price = document.getElementById("price");
let addBtn = document.getElementById("add-product");
let updateBtn = document.getElementById("update-product");
let loadAllBtn = document.getElementById("load-product");
let tableContent = document.getElementById("tbody");

addBtn.addEventListener("click", addHandler);
updateBtn.addEventListener("click", updateHandler);
loadAllBtn.addEventListener("click", loadAllHandler);
let updateProductId;

async function addHandler(event) {
    if (event) {
        event.preventDefault();
    }
    if (product.value === "" || count.value === "" || price.value === "") {
        return;
    }
    try {
        let body = { 
            product: product.value,
            count: count.value,
            price: price.value
        }
        let httpHeaders = {
            method: "POST",
            body: JSON.stringify(body)
        }
        await fetch(BASE_URL, httpHeaders);
        loadAllHandler();
        product.value = "";
        count.value = "";
        price.value = "";

    }
    catch (error) {
        console.log(error);
    }

}

async function loadAllHandler(event) {
    if (event) {
        event.preventDefault();
    }
    tableContent.innerHTML = "";
    try {
        const response = await fetch(BASE_URL);
        const data = await response.json();
        let groceries = Object.values(data);
        for (const {product, count, price, _id} of groceries) {
            let tr = createDOMElement("tr", tableContent, null, null, _id);
            createDOMElement("td", tr, product, ["name"]);
            createDOMElement("td", tr, count, ["count-product"]);
            createDOMElement("td", tr, price, ["product-price"]);
            let tdBtn = createDOMElement("td", tr, null, ["btn"]);
            let updateProductBtn = createDOMElement("button", tdBtn, "Update", ["update"]);
            let deleteProductBtn = createDOMElement("button", tdBtn, "Delete", ["delete"]);

            updateProductBtn.addEventListener("click", updateProductHandler);
            deleteProductBtn.addEventListener("click", deleteProductHandler);
        }
    }
    catch (error) {
        console.log(error);
    }
}

async function deleteProductHandler(event) {
    let btn = event.currentTarget;
    let productContainer = btn.parentElement.parentElement;
    let productId = productContainer.id;
    try {
        let httpHeaders = {
            method: "DELETE"
        }
        await fetch(`${BASE_URL}${productId}`, httpHeaders);
    }
    catch (error) {
        console.log(error);
    } 
    loadAllHandler();
}

function updateProductHandler(event) {
    updateBtn.removeAttribute("disabled");
    let btn = event.currentTarget;
    let productContainer = btn.parentElement.parentElement;
    updateProductId = productContainer.id;
    let [productName, productCount, productPrice] = Array.from(productContainer.children);
    product.value = productName.textContent;
    count.value = productCount.textContent;
    price.value = productPrice.textContent;
}

async function updateHandler(event) {
    if (event) {
        event.preventDefault();
    }
    if (product.value === "" || count.value === "" || price.value === "") {
        return;
    }
    try {
        let body = { 
            product: product.value,
            count: count.value,
            price: price.value
        }
        let httpHeaders = {
            method: "PATCH",
            body: JSON.stringify(body)
        }
        await fetch(`${BASE_URL}${updateProductId}`, httpHeaders);
        loadAllHandler();
        product.value = "";
        count.value = "";
        price.value = "";
        updateBtn.setAttribute("disabled", true);

    }
    catch (error) {
        console.log(error);
    }
}


function createDOMElement(type, parentElement, content, classes, id, attributes, useInnerHTML) {
    const newElement = document.createElement(type);

    if (content && useInnerHTML) {
      newElement.innerHTML = content;
    } else {
      if (content && type !== "input") {
        newElement.textContent = content;
      }
      if (content && type === "input") {
        newElement.value = content;
      }
    }

    if (classes && classes.length > 0) {
      newElement.classList.add(...classes);
    }

    if (id) {
      newElement.id = id;
    }

    if (attributes) {
      for (const key in attributes) {
        newElement[key] = attributes[key];
      }
    }

    if (parentElement) {
      parentElement.appendChild(newElement);
    }
    return newElement;
  }
