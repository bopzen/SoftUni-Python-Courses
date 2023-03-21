function solve() {
   let boughtItems = []
   let totalPrice = 0;
   
   let addBtns = Array.from(document.getElementsByClassName("add-product"));
   let checkoutBtn = document.getElementsByClassName("checkout")[0];
   let textArea = document.getElementsByTagName("textarea")[0];
   for (let i = 0; i < addBtns.length; i++) {
      addBtns[i].addEventListener("click", function addProductHandler() {
         let name = document.querySelector(`body > div > div:nth-child(${i + 2}) > div.product-details > div`).textContent;
         let price = document.querySelector(`body > div > div:nth-child(${i + 2}) > div.product-line-price`).textContent;
         if (!boughtItems.includes(name)) {
            boughtItems.push(name);
         }
         let productPrice = Number(price);
         totalPrice += productPrice;
         textArea.value += `Added ${name} for ${productPrice.toFixed(2)} to the cart.\n`;   
      });
   }

   checkoutBtn.addEventListener("click", checkoutHandler);
   
   function checkoutHandler() {
      textArea.value += `You bought ${boughtItems.join(", ")} for ${totalPrice.toFixed(2)}.`;
      disableButtons();
   }

   function disableButtons() {
      let buttons = Array.from(document.querySelectorAll('button'));
      buttons.forEach(button => button.disabled = true);
  }
}