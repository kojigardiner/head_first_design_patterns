from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        self.bark()

    def bark(self):
        print("woof!")


class Cat(Animal):
    def make_sound(self):
        self.meow()

    def meow(self):
        print("meow...")


d = Dog()
d.bark()

c = Cat()
c.meow()

animals = [Dog(), Cat(), Cat(), Dog()]

for animal in animals:
    animal.make_sound()
