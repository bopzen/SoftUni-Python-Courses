import os
from datetime import timedelta, date

import django



# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions
from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Registration, Car, Owner


def show_all_authors_with_their_books():
    result = []
    authors = Author.objects.all()
    for author in authors:
        books = author.book_set.all()
        if books:
            books_list = ", ".join(b.title for b in books)
            result.append(f'{author.name} has written - {books_list}!')
    return "\n".join(result)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    songs = artist.songs.all().order_by('-id')
    return songs


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)
    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()
    sum_rating = sum(r.rating for r in reviews)
    average_rating = sum_rating/reviews.count()
    return average_rating


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.all().order_by("-license_number")
    result = [
        f"License with id: {l.license_number} expires on {l.issue_date + timedelta(365)}!"
        for l in licenses
    ]
    return "\n".join(result)


def get_drivers_with_expired_licenses(due_date):
    date_before = due_date - timedelta(365)
    return Driver.objects.filter(drivinglicense__issue_date__gt=date_before)


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(owner=owner, registration__isnull=True).first()
    car.owner = owner
    car.registration = registration
    car.save()
    registration.registration_date = date.today()
    registration.car = car
    registration.save()
    return f'Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}.'


