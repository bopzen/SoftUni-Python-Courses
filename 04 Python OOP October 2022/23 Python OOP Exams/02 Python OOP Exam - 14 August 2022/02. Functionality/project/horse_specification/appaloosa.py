from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_SPEED = 120
    SPEED_ADD = 2

    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        self.speed = min(self.speed + self.SPEED_ADD, self.MAX_SPEED)