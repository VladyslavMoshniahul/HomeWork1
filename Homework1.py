from abc import abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class CarnivorousAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return "Meat"


class HerbivorousAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return "Plants"


class OmnivorousAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        return "All"


class Bear(OmnivorousAnimal):
    def speak(self):
        return "Arrh"


class Wolf(CarnivorousAnimal):
    def speak(self):
        return "Woof"


class Rabbit(HerbivorousAnimal):
    def speak(self):
        return "Squeak"


class Zoo:
    def __init__(self):
        self.bear = Bear("Brown Bear")
        self.wolf = Wolf("Grey Wolf")
        self.rabbit = Rabbit("White Rabbit")

    def display_info(self):
        print("Bear:")
        print("Name:", self.bear.name)
        print("Speak:", self.bear.speak())
        print("Eat:", self.bear.eat())
        print()

        print("Wolf:")
        print("Name:", self.wolf.name)
        print("Speak:", self.wolf.speak())
        print("Eat:", self.wolf.eat())
        print()

        print("Rabbit:")
        print("Name:", self.rabbit.name)
        print("Speak:", self.rabbit.speak())
        print("Eat:", self.rabbit.eat())


zoo = Zoo()
zoo.display_info()
