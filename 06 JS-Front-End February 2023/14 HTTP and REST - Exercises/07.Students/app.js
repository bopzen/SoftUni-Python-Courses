function attachEvents() {
  const BASE_URL = "http://localhost:3030/jsonstore/collections/students";

  let submitBtn = document.getElementById("submit");
  let [firstName, lastName, facultyNumber, grade] = Array.from(document.querySelectorAll(".inputs input"));
  let studentsTable = document.getElementsByTagName("tbody")[0];
  showStudents();
  submitBtn.addEventListener("click", submitHandler);


  async function submitHandler() {
    let newStudent = {
      firstName: firstName.value, 
      lastName: lastName.value, 
      facultyNumber: facultyNumber.value, 
      grade: grade.value
    };
    let httpHeader  = {
      method: "post",
      body: JSON.stringify(newStudent)
    }
    
    let resData = await fetch(BASE_URL, httpHeader);
    showStudents();
  }


  async function showStudents() {
    studentsTable.innerHTML = "";

    let response = await fetch(BASE_URL);
    let data = await response.json();
    let studentsList = Object.values(data);
    console.log(studentsList)
    for (const {firstName, lastName, facultyNumber, grade} of studentsList) {
      let newRow = document.createElement("tr");

      let newTd = document.createElement("td");
      newTd.textContent = firstName;
      newRow.appendChild(newTd);

      newTd = document.createElement("td");
      newTd.textContent = lastName;
      newRow.appendChild(newTd);

      newTd = document.createElement("td");
      newTd.textContent = facultyNumber;
      newRow.appendChild(newTd);

      newTd = document.createElement("td");
      newTd.textContent = grade;
      newRow.appendChild(newTd);

      studentsTable.appendChild(newRow);
    }
  }
}

attachEvents();