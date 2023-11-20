from django.core import validators
from django.db import models

from main_app.managers import DirectorManager
from main_app.mixins import LastUpdatedMixin, IsAwardedMixin


class BaseEmployee(models.Model):
    class Meta:
        abstract = True

    full_name = models.CharField(
        max_length=120,
        validators=(
            validators.MinLengthValidator(2),
        )
    )
    birth_date = models.DateField(
        default='1900-01-01',
    )
    nationality = models.CharField(
        max_length=50,
        default='Unknown',
    )

    def __str__(self):
        return self.full_name


class Director(BaseEmployee):
    years_of_experience = models.SmallIntegerField(
        validators=(
            validators.MinValueValidator(0),
        ),
        default=0,
    )

    objects = DirectorManager()


class Actor(LastUpdatedMixin, IsAwardedMixin, BaseEmployee):
    pass


class Movie(LastUpdatedMixin, IsAwardedMixin):
    GENRES = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Other', 'Other'),
    ]
    title = models.CharField(
        max_length=150,
        validators=(
            validators.MinLengthValidator(5),
        )
    )
    release_date = models.DateField()
    storyline = models.TextField(
        null=True,
        blank=True,
    )
    genre = models.CharField(
        max_length=6,
        choices=GENRES,
        default='Other'
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=(
            validators.MinValueValidator(0),
            validators.MaxValueValidator(10),
        ),
        default=0,
    )
    is_classic = models.BooleanField(
        default=False,
    )
    is_awarded = models.BooleanField(
        default=False,
    )
    last_updated = models.DateTimeField(
        auto_now=True,
    )
    director = models.ForeignKey(
        to=Director,
        related_name='director_movies',
        on_delete=models.CASCADE,
    )
    starring_actor = models.ForeignKey(
        to=Actor,
        related_name='starring_movies',
        on_delete=models.SET_NULL,
        null=True,
    )
    actors = models.ManyToManyField(
        to=Actor,
        related_name='actor_movies'
    )

    def __str__(self):
        return self.title
