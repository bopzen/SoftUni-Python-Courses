function solve(input) {
    let shelves = [];
    for (const line of input) {
        if (line.includes("->")) {
            let [newId, genre] = line.split(" -> ");
            let exists = false;
            for (const shelf of shelves) {
                if (shelf.id === newId) {
                    exists = true;
                    break;
                }
            }
            if (exists == false) {
                let newShelf = {id: newId, genre: genre, books: []};
                shelves.push(newShelf);
            }     
        } else {
            let [bookTitle, bookinfo] = line.split(": ");
            let [bookAuthor, bookGenre] = bookinfo.split(", ");
            let exists = false;
            for (const shelf of shelves) {
                if (shelf.genre === bookGenre) {
                    let newBook = {bookTitle, bookAuthor, bookGenre};
                    shelf.books.push(newBook)
                    break;
                }
            }
        }
    }
    for (const shelf of shelves.sort((a,b) => b.books.length - a.books.length)) {
        console.log(`${shelf.id} ${shelf.genre}: ${shelf.books.length}`);
        for (const book of shelf.books.sort((a,b) => a.bookTitle.localeCompare(b.bookTitle))) {
            console.log(`--> ${book.bookTitle}: ${book.bookAuthor}`);
        }
    }
}

solve(['1 -> history', '1 -> action', 'Death in Time: Criss Bell, mystery', '2 -> mystery', '3 -> sci-fi', 'Child of Silver: Bruce Rich, mystery', 'Hurting Secrets: Dustin Bolt, action', 'Future of Dawn: Aiden Rose, sci-fi', 'Lions and Rats: Gabe Roads, history', '2 -> romance', 'Effect of the Void: Shay B, romance', 'Losing Dreams: Gail Starr, sci-fi', 'Name of Earth: Jo Bell, sci-fi', 'Pilots of Stone: Brook Jay, history']);

solve(['1 -> mystery', '2 -> sci-fi',
'Child of Silver: Bruce Rich, mystery',
'Lions and Rats: Gabe Roads, history',
'Effect of the Void: Shay B, romance',
'Losing Dreams: Gail Starr, sci-fi',
'Name of Earth: Jo Bell, sci-fi']
);
