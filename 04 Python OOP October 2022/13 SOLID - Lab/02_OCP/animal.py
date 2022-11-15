from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):

    def make_sound(self):
        return "Woof"


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())
