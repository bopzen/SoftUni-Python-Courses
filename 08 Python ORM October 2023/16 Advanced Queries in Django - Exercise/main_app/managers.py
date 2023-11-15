from django.db import models
from django.db.models import Count, Max, Min, Avg


class RealEstateListingManager(models.Manager):
    def by_property_type(self, property_type):
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price, max_price):
        return self.filter(price__range=(min_price, max_price))

    def with_bedrooms(self, bedrooms_count):
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self):
        return self.values('location').annotate(visits=Count('id')).order_by('id')[:2]


class VideoGameManager(models.Manager):
    def games_by_genre(self, genre):
        return self.filter(genre=genre)

    def recently_released_games(self, year):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        highest_rating = self.aggregate(max_rate=Max('rating'))['max_rate']
        highest_rated_game = self.filter(rating=highest_rating).first()
        return highest_rated_game

    def lowest_rated_game(self):
        lowest_rating = self.aggregate(min_rate=Min('rating'))['min_rate']
        lowest_rated_game = self.filter(rating=lowest_rating).first()
        return lowest_rated_game

    def average_rating(self):
        return f"{self.aggregate(average_rating=Avg('rating'))['average_rating']:.1f}"