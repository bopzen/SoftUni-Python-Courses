function search() {
   let towns = document.getElementById("towns");
   let searchInput = document.getElementById("searchText");
   let result = document.getElementById("result");
   let searchedText = searchInput.value;
   let matches = 0;
   for (const town of Array.from(towns.children)) {
      if (town.textContent.includes(searchedText)) {
         town.style.fontWeight = "bold";
         town.style.textDecoration = "underline";
         matches++;
      } else {
         town.style.fontWeight = "normal";
         town.style.textDecoration = "none";
      }
   }
   result.textContent = `${matches} matches found`;
}
