from abc import ABC, abstractmethod
from enum import Enum

# Base classes


class Beverage(ABC):
    class Size(Enum):
        TALL = (1,)
        GRANDE = (2,)
        VENTI = 3

    description: str = "Unknown Beverage"
    size: Size = Size.TALL

    def get_description(self) -> str:
        return self.description

    def set_size(self, size: Size):
        self.size = size

    def get_size(self) -> Size:
        return self.size

    @abstractmethod
    def cost(self) -> float:
        raise NotImplementedError


class CondimentDecorator(Beverage):
    beverage: Beverage

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError


# Beverages


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self) -> float:
        return 0.99


class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf Coffee"

    def cost(self) -> float:
        return 1.05


# Condiments


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Mocha"

    def cost(self) -> float:
        return self.beverage.cost() + 0.20


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Soy"

    def cost(self) -> float:
        adder = 0.15
        if self.beverage.get_size() == Beverage.Size.TALL:
            adder = 0.10
        elif self.beverage.get_size() == Beverage.Size.GRANDE:
            adder = 0.15
        elif self.beverage.get_size() == Beverage.Size.VENTI:
            adder = 0.20

        return self.beverage.cost() + adder


class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def get_description(self) -> str:
        return self.beverage.get_description() + ", Whip"

    def cost(self) -> float:
        return self.beverage.cost() + 0.10


# test

if __name__ == "__main__":
    beverage: Beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.cost()))

    beverage2: Beverage = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.cost()))

    beverage3: Beverage = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description() + " $" + str(beverage3.cost()))
