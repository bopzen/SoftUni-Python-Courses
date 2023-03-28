async function lockedProfile() {
    try {
        let response = await fetch("http://localhost:3030/jsonstore/advanced/profiles/");
        let data = await response.json();
    
        let main = document.getElementById("main");
        main.innerHTML = "";
        let users = Object.values(data);
        let counter = 1;
        for (const user of users) {
            const wrapper = document.createElement('div')
            const showBtn = document.createElement('button')
            showBtn.innerText = 'Show more'
        
            wrapper.className = 'profile'
            wrapper.innerHTML = `<img src="./iconProfile2.png" class="userIcon">
        <label>Lock</label>
        <input type="radio" name="user${counter}-Locked" value="lock" checked="">
        <label>Unlock</label>
        <input type="radio" name="user${counter}-Locked" value="unlock"><br>
        <hr>
        <label>Username</label>
        <input type="text" name="user${counter}Username" value=${user.username} disabled="" readonly="">
        <div class="hiddenInfo">
        <hr>
        <label>Email:</label>
        <input type="email" name="user${counter}Email" value=${user.email} disabled="" readonly="">
        <label>Age:</label>
        <input type="email" name="user${counter}Age" value=${user.age} disabled="" readonly="">
        </div>`
            
            showBtn.addEventListener("click", showMoreHandler);    
            wrapper.appendChild(showBtn);
            main.appendChild(wrapper);  

            counter++;
        }
    }
    catch (error) {
        console.log(error);
    }
}

function showMoreHandler(event) {
    let element = event.currentTarget;
    let hiddenElement = Array.from(element.parentElement.querySelectorAll(".hiddenInfo > input, .hiddenInfo > label"));
    let locked = element.parentElement.querySelector('input[value="lock"]');
    if (element.textContent === "Show more") {
        if (!locked.checked) {
            element.textContent = "Hide it";
            for (const hidden of hiddenElement) {
                hidden.style.display = "block";
            }             
        }
    } else if (element.textContent === "Hide it") {
        if (!locked.checked) {
            element.textContent = "Show more";
            for (const hidden of hiddenElement) {
                hidden.style.display = "none";
            }  
        }
    }
}

