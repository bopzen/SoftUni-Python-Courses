import os
import django
from django.db.models import Count, Avg, Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# Create and run your queries within functions
from main_app.models import Director, Actor, Movie


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    query_name = Q(full_name__icontains=search_name)
    query_nationality = Q(nationality__icontains=search_nationality)

    if search_name is not None and search_nationality is not None:
        query = query_name & query_nationality
    elif search_name is not None:
        query = query_name
    else:
        query = query_nationality

    directors = Director.objects.filter(query).order_by('full_name')

    if not directors:
        return ""

    result = [
        f"Director: {director.full_name}, nationality: {director.nationality}, experience: {director.years_of_experience}"
        for director in directors
    ]
    return '\n'.join(result)


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()
    if top_director:
        return f"Top Director: {top_director.full_name}, movies: {top_director.movies_count}."
    return ""


def get_top_actor():
    top_actor = Actor.objects.annotate(
        movies_count=Count('starring_movies'),
        average_rating=Avg('starring_movies__rating')
    ).order_by(
        '-movies_count', 'full_name'
    ).first()
    if not top_actor or not top_actor.movies_count:
        return ""
    movies_list = ", ".join(movie.title for movie in top_actor.starring_movies.all() if movie)
    return f"Top Actor: {top_actor.full_name}, starring in movies: {movies_list}, movies average rating: {top_actor.average_rating:.1f}"


def get_actors_by_movies_count():
    top_three_actors = Actor.objects.annotate(
        movies_count=Count('actor_movies'),
    ).order_by(
        '-movies_count', 'full_name'
    )[:3]
    if not top_three_actors or not top_three_actors[0].movies_count:
        return ""
    result = [
        f"{actor.full_name}, participated in {actor.movies_count} movies"
        for actor in top_three_actors
    ]
    return "\n".join(result)


def get_top_rated_awarded_movie():
    top_movie = Movie.objects.select_related(
        'starring_actor'
    ).prefetch_related(
        'actors'
    ).filter(
        is_awarded=True
    ).order_by(
        '-rating',
        'title'
    ).first()

    if top_movie is None:
        return ""
    starring_actor = top_movie.starring_actor.full_name if top_movie.starring_actor else "N/A"
    cast = ", ".join(actor.full_name for actor in top_movie.actors.order_by('full_name'))

    return f"Top rated awarded movie: {top_movie.title}, rating: {top_movie.rating:.1f}. " \
           f"Starring actor: {starring_actor}. Cast: {cast}."


def increase_rating():
    movies_to_update = Movie.objects.filter(is_classic=True, rating__lt=10.0)
    if not movies_to_update:
        return "No ratings increased."

    num_of_updated_movies = movies_to_update.update(rating=F('rating') + 0.1)
    return f"Rating increased for {num_of_updated_movies} movies."

