from abc import ABC, abstractmethod
from math import log2, ceil, floor


class Computer(ABC):
    AVAILABLE_PROCESSORS = {}

    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    def manufacturer(self):
        return self.__manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @staticmethod
    def power_of_two(n):
        result = log2(n)
        return floor(result) == ceil(result)

    @abstractmethod
    def configure_computer(self, processor, ram):
        pass

    def set_computer(self, processor, ram):
        self.processor = processor
        self.ram = ram
        self.price += self.AVAILABLE_PROCESSORS[processor]
        self.price += int(log2(ram)) * 100

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"