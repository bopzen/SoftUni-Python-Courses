import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Person
# Import your models here

# Create queries within functions

person = Person(
    name='Ivan',
    age=15
)
person.save()