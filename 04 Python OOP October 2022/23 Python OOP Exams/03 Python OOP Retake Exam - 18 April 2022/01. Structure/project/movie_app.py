from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __check_user(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def register_user(self, username, age):
        if self.__check_user(username):
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie):
        if not self.__check_user(username):
            raise Exception("This user does not exist!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.append(movie)
        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.append(movie)
                return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        for key, value in kwargs.items():
            setattr(movie, key, value)
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        for user in self.users_collection:
            if user.username == username:
                user.movies_owned.remove(movie)
                return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username, movie):
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        for user in self.users_collection:
            if user.username == username:
                if movie in user.movies_liked:
                    raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.append(movie)
                return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie):
        for user in self.users_collection:
            if user.username == username:
                if movie not in user.movies_liked:
                    raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        for user in self.users_collection:
            if user.username == username:
                user.movies_liked.remove(movie)
                return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."
        result = []
        for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
            result.append(movie.details())
        return "\n".join(result)

    def __str__(self):
        if len(self.users_collection) == 0:
            users = 'No users.'
        else:
            users = ', '.join([user.username for user in self.users_collection])
        if len(self.movies_collection) == 0:
            movies = 'No movies.'
        else:
            movies = ', '.join([movie.title for movie in self.movies_collection])
        return f"All users: {users}\nAll movies: {movies}"


