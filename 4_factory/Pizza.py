from abc import ABC, abstractmethod
from typing import List

# Pizzas


class Pizza(ABC):
    name: str
    dough: str
    sauce: str
    veggies: List[Veggies]
    cheese: Cheese
    pepperoni: Pepperoni
    clams: Clam

    @abstractmethod
    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print("Bake for 25 minutes at 350°F")

    def cut(self):
        print("Cutting the pizza into diagnoal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name


class CheesePizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.get_name()}")

        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory):
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"Preparing {self.get_name()}")

        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings = []
        self.toppings.append("Grated Reggiano Cheese")


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"
        self.toppings = []
        self.toppings.append("Shredded Mozzarella Cheese")

    def cut(self):
        print("Cutting the pizza into square slices")


# PizzaStore


class PizzaStore(ABC):
    @abstractmethod
    def create_pizza(self, type: str) -> Pizza:
        raise NotImplementedError

    def order_pizza(self, type: str) -> Pizza:
        pizza: Pizza = self.create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> Pizza:
        pizza: Pizza
        ingredient_factory: PizzaIngredientFactory = NYPizzaIngredientFactory()
        if type == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")
            # pizza = NYStyleCheesePizza()
        elif type == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")
            # pizza = NYStyleVeggiePizza()
        elif type == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")
            # pizza = NYStyleClamPizza()
        elif type == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")
            # pizza = NYStylePepperoniPizza()
        else:
            pizza = None

        return pizza


class CAPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> Pizza:
        pizza: Pizza
        if type == "cheese":
            pizza = CAStyleCheesePizza()
        elif type == "veggie":
            pizza = CAStyleVeggiePizza()
        elif type == "clam":
            pizza = CAStyleClamPizza()
        elif type == "pepperoni":
            pizza = CAStylePepperoniPizza()
        else:
            pizza = None

        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type: str) -> Pizza:
        pizza: Pizza
        if type == "cheese":
            pizza = ChicagoStyleCheesePizza()
        elif type == "veggie":
            pizza = ChicagoStyleVeggiePizza()
        elif type == "clam":
            pizza = ChicagoStyleClamPizza()
        elif type == "pepperoni":
            pizza = ChicagoStylePepperoniPizza()
        else:
            pizza = None

        return pizza


# Ingredients
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough:
        raise NotImplementedError

    @abstractmethod
    def create_sauce(self) -> Sauce:
        raise NotImplementedError

    @abstractmethod
    def create_cheese(self) -> Cheese:
        raise NotImplementedError

    @abstractmethod
    def create_veggies(self) -> List[Veggies]:
        raise NotImplementedError

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        raise NotImplementedError

    @abstractmethod
    def create_clam(self) -> Clam:
        raise NotImplementedError


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> List[Veggies]:
        veggies: List[Veggies] = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clam:
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()

    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()

    def create_veggies(self) -> List[Veggies]:
        veggies: List[Veggies] = [Spinach(), BlackOlives(), Eggplant()]
        return veggies

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clam:
        return FrozenClams()


if __name__ == "__main__":
    ny_store: PizzaStore = NYPizzaStore()
    ch_store: PizzaStore = ChicagoPizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Ethan ordered a {pizza.get_name()}")

    pizza = ch_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza.get_name()}")
