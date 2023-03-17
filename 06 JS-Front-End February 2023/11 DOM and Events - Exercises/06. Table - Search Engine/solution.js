function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let rows = document.querySelectorAll("table tr");
      let searchBox = document.getElementById("searchField");
      let searchedText = searchBox.value;
      console.log(rows)
      for (const row of rows) {
         let text = row.textContent;
         if (row.classList.contains("select")) {
            row.classList.remove("select");
         }
         if (text.includes(searchedText)) {
            row.classList.add("select")
         }
      }
      searchBox.value = "";
   }
}