window.addEventListener('load', solve);

function solve() {
    let allHits = document.querySelector(".all-hits-container");
    let savedHits = document.querySelector(".saved-container");
    let totalLikes = document.querySelector(".likes p");
    let genre = document.getElementById("genre");
    let name = document.getElementById("name");
    let author = document.getElementById("author");
    let date = document.getElementById("date");
    let addBtn = document.getElementById("add-btn")   ;
    addBtn.addEventListener("click", addHandler); 



    function addHandler(e) {
        e.preventDefault();
        if (genre.value === ""
            || name.value === ""
            || author.value === ""
            || date.value === "") {
                return
            }
        let hitsInfo = createDOMElement("div", allHits, null, ["hits-info"]);
        createDOMElement("img", hitsInfo, null, null, null, {"src": "./static/img/img.png"});
        createDOMElement("h2", hitsInfo, `Genre: ${genre.value}`);
        createDOMElement("h2", hitsInfo, `Name: ${name.value}`);
        createDOMElement("h2", hitsInfo, `Author: ${author.value}`);
        createDOMElement("h3", hitsInfo, `Date: ${date.value}`);
        let saveBtn = createDOMElement("button", hitsInfo, "Save song", ["save-btn"]);
        let likeBtn = createDOMElement("button", hitsInfo, "Like song", ["like-btn"]);
        let deleteBtn = createDOMElement("button", hitsInfo, "Delete", ["delete-btn"]);
        
        saveBtn.addEventListener("click", saveHandler);
        likeBtn.addEventListener("click", likeHandler);
        deleteBtn.addEventListener("click", deleteHandler);
        
        genre.value = "";
        name.value = "";
        author.value = "";
        date.value = "";
    }

    function saveHandler(event) {
        let btn = event.currentTarget;
        let songInfo = btn.parentElement;
        songInfo.removeChild(songInfo.querySelector(".save-btn"));
        songInfo.removeChild(songInfo.querySelector(".like-btn"));
        let savedSongInfo = songInfo.cloneNode(true);
        savedHits.appendChild(savedSongInfo);
        songInfo.remove();
        savedSongInfo.querySelector(".delete-btn").addEventListener("click", deleteHandler);

    }   

    function likeHandler(event) {
        let btn = event.currentTarget;
        let likes = Number(totalLikes.textContent.split(" ")[2]);
        likes++;
        totalLikes.textContent = `Total Likes: ${likes}`;
        btn.setAttribute("disabled", true);
    }   

    function deleteHandler(event) {
        let btn = event.currentTarget;
        let songInfo = btn.parentElement;
        songInfo.remove();
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
}