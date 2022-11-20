from project.animals.animal import Bird

from project.food import Meat

from project.food import Vegetable

from project.food import Fruit

from project.food import Seed


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit, Seed, Meat]
    
    @property
    def gained_weight(self):
        return 0.35

    def make_sound(self):
        return "Cluck"



