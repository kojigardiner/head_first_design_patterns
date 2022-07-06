from abc import ABC, abstractmethod

# Duck


class Duck(ABC):
    fly_behavior: "FlyBehavior"
    quack_behavior: "QuackBehavior"

    @abstractmethod
    def display(self):
        raise NotImplementedError

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def set_fly_behavior(self, fb):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb):
        self.quack_behavior = qb

    def swim(self):
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck")


# FlyBehavior


class FlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


# QuackBehavior


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class DuckCallQuack(QuackBehavior):
    def quack(self):
        print("<< fake quack >>")


# Duck call
class DuckCall:
    quack_behavior = DuckCallQuack()

    def perform_quack(self):
        self.quack_behavior.quack()


if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()

    dc = DuckCall()
    dc.perform_quack()
