import os
import django
from datetime import date

from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries
from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


def create_pet(name: str, species: str):
    pet = Pet.objects.create(
        name=name,
        species=species
    )
    return f'{pet.name} is a very cute {pet.species}!'


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )
    return f'The artifact {artifact.name} is {artifact.age} years old!'


def delete_all_artifacts():
    Artifact.objects.all().delete()


def show_all_locations():
    all_locations = Location.objects.all().order_by('-id')
    return '\n'.join(f'{l.name} has a population of {l.population}!' for l in all_locations)


def new_capital():
    location = Location.objects.first()
    location.is_capital = True
    location.save()


def get_capitals():
    return Location.objects.filter(is_capital=True).values('name')


def delete_first_location():
    Location.objects.first().delete()


def apply_discount():
    all_cars = Car.objects.all()
    for car in all_cars:
        discount_percentage = sum(int(d) for d in str(car.year)) / 100
        car.price_with_discount = float(car.price) - float(car.price) * discount_percentage
        car.save()


def get_recent_cars():
    return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car():
    Car.objects.last().delete()


def show_unfinished_tasks():
    unfinished_tasks = Task.objects.filter(is_finished=False)
    return '\n'.join(f'Task - {ut.title} needs to be done until {ut.due_date}!' for ut in unfinished_tasks)


def complete_odd_tasks():
    for task in Task.objects.all():
        if task.id % 2 != 0:
            task.is_finished = True
            task.save()


def encode_and_replace(text: str, task_title: str):
    tasks = Task.objects.filter(title=task_title)
    for task in tasks:
        task.description = ''.join(chr(ord(x) - 3) for x in text)
        task.save()


def get_deluxe_rooms():
    all_deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
    return '\n'.join(f'Deluxe room with number {r.room_number} costs {r.price_per_night}$ per night!' for r in all_deluxe_rooms if r.id % 2 == 0)


def increase_room_capacity():
    all_rooms = HotelRoom.objects.all().order_by('id')
    previous_room_capacity = None
    for room in all_rooms:
        if not room.is_reserved:
            continue
        if previous_room_capacity:
            room.capacity += previous_room_capacity
        else:
            room.capacity += room.id
        previous_room_capacity = room.capacity
        room.save()


def reserve_first_room():
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room():
    last_room = HotelRoom.objects.last()
    if last_room.is_reserved:
        last_room.delete()


def update_characters() -> None:
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4,
    )

    Character.objects.filter(class_name__in=["Assassin", "Scout"]).update(
        inventory="The inventory is empty",
    )


def fuse_characters(first_character: Character, second_character: Character) -> None:
    fusion_name = first_character.name + " " + second_character.name
    fusion_level = (first_character.level + second_character.level) // 2
    fusion_class = "Fusion"
    fusion_strength = (first_character.strength + second_character.strength) * 1.2
    fusion_dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    fusion_intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    fusion_hit_points = (first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ["Mage", "Scout"]:
        fusion_inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        fusion_inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=fusion_name,
        class_name=fusion_class,
        level=fusion_level,
        strength=fusion_strength,
        dexterity=fusion_dexterity,
        intelligence=fusion_intelligence,
        hit_points=fusion_hit_points,
        inventory=fusion_inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity() -> None:
    Character.objects.update(dexterity=30)


def grand_intelligence() -> None:
    Character.objects.update(intelligence=40)


def grand_strength() -> None:
    Character.objects.update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory="The inventory is empty").delete()