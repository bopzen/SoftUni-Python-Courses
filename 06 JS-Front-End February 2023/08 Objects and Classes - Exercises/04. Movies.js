function solve(input) {
    let movies = [];
    for (let command of input) {
        if (command.includes("addMovie")) {
            command = command.replace("addMovie ","");
            let movie = {name: command};
            movies.push(movie);
        } else if (command.includes("directedBy")) {
            let [name, director] = command.split(" directedBy ");
            for (const movie of movies) {
                if (movie.name == name) {
                    movie.director = director;
                    break;
                }
            }
        } else if (command.includes("onDate")) {
            let [name, date] = command.split(" onDate ");
            for (const movie of movies) {
                if (movie.name == name) {
                    movie.date = date;
                    break;
                }
            }
        }
    }
    for (let movie of movies) {
        if (movie.name && movie.director && movie.date) {
            let result = JSON.stringify(movie);
            console.log(result);
        }
    }
}

solve([
    'addMovie Fast and Furious',
    'addMovie Godfather',
    'Inception directedBy Christopher Nolan',
    'Godfather directedBy Francis Ford Coppola',
    'Godfather onDate 29.07.2018',
    'Fast and Furious onDate 30.07.2018',
    'Batman onDate 01.08.2018',
    'Fast and Furious directedBy Rob Cohen'
    ]
    );

solve([
    'addMovie The Avengers',
    'addMovie Superman',
    'The Avengers directedBy Anthony Russo',
    'The Avengers onDate 30.07.2010',
    'Captain America onDate 30.07.2010',
    'Captain America directedBy Joe Russo'
    ]
    );