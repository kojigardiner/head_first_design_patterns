from abc import ABC, abstractmethod, abstractproperty
from re import L

# Characters


class Character(ABC):
    weapon: "WeaponBehavior"  # character HAS-A weapon behavior

    @abstractmethod
    def fight(self):
        raise NotImplementedError

    def set_weapon(self, wb):
        self.weapon = wb


class Queen(Character):  # inherits from Character
    def __init__(self):
        self.weapon = KnifeBehavior()

    def fight(self):
        print("I'm the queen and I'll hurt you!")
        self.weapon.use_weapon()


class King(Character):  # inherits from Character
    def __init__(self):
        self.weapon = SwordBehavior()

    def fight(self):
        print("I'm the king and I'll subject you!")
        self.weapon.use_weapon()


class Knight(Character):  # inherits from Character
    def __init__(self):
        self.weapon = BowAndArrowBehavior()

    def fight(self):
        print("I'm a lowly knight")
        self.weapon.use_weapon()


class Troll(Character):  # inherits from Character
    def __init__(self):
        self.weapon = AxeBehavior()

    def fight(self):
        print("I'm a troll and I'll club you!")
        self.weapon.use_weapon()


# Weapon Behaviors


class WeaponBehavior(ABC):
    @abstractmethod
    def use_weapon(self):
        raise NotImplementedError


class KnifeBehavior(WeaponBehavior):  # implements WeaponBehavior
    def use_weapon(self):
        print("Cutting with a knife!")


class BowAndArrowBehavior(WeaponBehavior):  # implements WeaponBehavior
    def use_weapon(self):
        print("Shooting an arrow with a bow!")


class AxeBehavior(WeaponBehavior):  # implements WeaponBehavior
    def use_weapon(self):
        print("Chopping with an axe!")


class SwordBehavior(WeaponBehavior):  # implements WeaponBehavior
    def use_weapon(self):
        print("Swinging a sword!")


if __name__ == "__main__":
    q = Queen()
    k = King()
    n = Knight()
    t = Troll()

    q.fight()
    k.fight()
    n.fight()
    t.fight()

    print("The queen changes weapons!")
    q.set_weapon(AxeBehavior())
    q.fight()
