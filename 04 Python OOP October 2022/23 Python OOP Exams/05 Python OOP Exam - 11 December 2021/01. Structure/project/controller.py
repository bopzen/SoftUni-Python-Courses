from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type, model, speed_limit):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")
        if car_type == 'MuscleCar':
            new_car = MuscleCar(model, speed_limit)
        elif car_type == 'SportsCar':
            new_car = SportsCar(model, speed_limit)
        else:
            return
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        try:
            driver = next(filter(lambda x: x.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")
        try:
            car = list(filter(lambda x: x.__class__.__name__ == car_type and not x.is_taken, self.cars))[-1]
        except IndexError:
            raise Exception(f"Car {car_type} could not be found!")
        if driver.car:
            old_car = driver.car
            driver.car = car
            car.is_taken = True
            old_car.is_taken = False
            return f"Driver {driver_name} changed his car from {old_car.model} to {car.model}."
        else:
            driver.car = car
            car.is_taken = True
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name, driver_name):
        try:
            race = next(filter(lambda x: x.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")
        try:
            driver = next(filter(lambda x: x.name == driver_name, self.drivers))
        except StopIteration:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        try:
            race = next(filter(lambda x: x.name == race_name, self.races))
        except StopIteration:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        sorted_drivers = list(sorted(race.drivers, key=lambda x: -x.car.speed_limit))[0:3]
        result = []
        for driver in sorted_drivers:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
        return "\n".join(result)
