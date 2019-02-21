class DomesticAnimal:
    species = None
    name = None
    position = None
    product = None
    voice = None
    meat = None

    def show_animal(self):
        show = (self.name + " находится - " + self.position)
        print(show)

    def use(self):
        print(self.name + " дает " + self.product)

    def says(self):
        print(self.name + " говорит " + self.voice)

    def meat_received(self):
        print(self.species, " дает", self.meat)


class Pet(DomesticAnimal):
    meat = "более 200кг мяса"


class Bird(DomesticAnimal):
    meat = "менее 6кг мяса"
    eggs = 0

    def lay_eggs(self, laid_egg):
        self.eggs += laid_egg
        print(self.name + " снесла " + self.product + " " + str(self.eggs) + "шт ")


class Cow(Pet):
    species = "Корова"

    def __init__(self, name, posision):
        self.name = name
        self.position = posision
    voice = "му-му"
    product = "коровье молоко"


class Gout(Pet):
    species = "Коза"

    def __init__(self, name, posision):
        self.name = name
        self.position = posision
    voice = "ме-ме"
    product = "козье молоко"


class Sheep(Pet):
    species = "Овца"

    def __init__(self, name, posision):
        self.name = name
        self.position = posision
    voice = "бе-бе"
    product = "шерсть"


class Pig(Pet):
    species = "Свинья"

    def __init__(self, name, posision):
        self.name = name
        self.position = posision
    voice = "хрю-хрю"
    product = "Сало"


class Chicken(Bird):
    species = "Курица"

    def __init__(self, name, posision):
        self.name = name
        self.position = posision
    voice = "ко-ко"
    product = "куриное яйцо"


class Guz(Bird):
    species = "Гусь"

    def __init__(self, name, posision):
        self.name = name
        self.position = posision

    voice = "га-га"
    product = "гусиное яйцо"


class Duck(Bird):
    species = "Утка"

    def __init__(self, name, posision):
        self.name = name
        self.position = posision

    voice = "кря-кря"
    product = "утиное яйцо"

