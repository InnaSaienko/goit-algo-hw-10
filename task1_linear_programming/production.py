from dataclasses import dataclass

from pulp import LpProblem, LpMaximize, LpVariable


@dataclass
class Drink:
    """Represents a drink and ingredients."""

    name: str
    ingredients: dict[str, int]


@dataclass
class Resources:
    """Holds available resources limits."""

    limits: dict[str, int]


class ProductionModel:
    """Solve production optimization problem."""

    def __init__(self, drinks: list[Drink], resources: Resources):
        self.model = LpProblem("Production", LpMaximize)
        self.vars = {drink.name: LpVariable(drink.name, lowBound=0, cat="Integer") for drink in drinks}
        self.model += sum(self.vars.values())


    def solve(self):
        self.model.solve()
        return {k: v.value() for k, v in self.vars.items()}
