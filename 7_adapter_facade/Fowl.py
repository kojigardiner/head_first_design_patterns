import random
from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self):
        raise NotImplementedError

    @abstractmethod
    def fly(self):
        raise NotImplementedError


class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        raise NotImplementedError

    @abstractmethod
    def fly(self):
        raise NotImplementedError


class MallardDuck(Duck):
    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm flying")


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")

    def fly(self):
        print("I'm flying a short distance")


class TurkeyAdapter(Duck):
    turkey: Turkey

    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()


class TurkeyClassAdapter(Turkey, Duck):
    def gobble(self):
        print("Gobble gobble")

    def quack(self):
        self.gobble()

    def fly(self):
        for i in range(5):
            print("I'm flying a short distance")


class DuckAdapter(Turkey):
    duck: Duck

    def __init__(self, duck):
        self.duck = duck

    def gobble(self):
        self.duck.quack()

    def fly(self):
        if random.randint(0, 4) == 0:
            self.duck.fly()


def test_duck(duck: Duck):
    duck.quack()
    duck.fly()


def test_turkey(turkey: Turkey):
    turkey.gobble()
    turkey.fly()


def test_duck_with_turkeyclassadapter(duck: Duck):
    duck.quack()
    duck.fly()


if __name__ == "__main__":
    duck = MallardDuck()
    turkey = WildTurkey()
    turkeyAdapter = TurkeyAdapter(turkey)
    turkeyClassAdapter = TurkeyClassAdapter()
    duckAdapter = DuckAdapter(duck)

    print("\nThe Turkey says...")
    turkey.gobble()
    turkey.fly()

    print("\nThe Duck says...")
    duck.quack()
    duck.fly()

    print("\nThe TurkeyAdapter says...")
    test_duck(turkeyAdapter)

    print("\nThe DuckAdapter says...")
    test_turkey(duckAdapter)

    print("\nThe TurkeyClassAdapter says...")
    test_duck_with_turkeyclassadapter(turkeyClassAdapter)
