function create(words) {
   for (const word of words) {
      let content = document.getElementById("content");
      let newDiv = document.createElement("div");
      let newP = document.createElement("p");
      newP.textContent = word;
      newP.style.display = "none";
      newDiv.addEventListener("click", clickMe)
      newDiv.appendChild(newP);
      content.appendChild(newDiv)
   }

   function clickMe(e) {
      let element = e.currentTarget;
      element.children[0].style.display = "";
   }
}