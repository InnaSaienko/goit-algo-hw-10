from dataclasses import dataclass

from pulp import LpProblem, LpMaximize, LpVariable


@dataclass
class Drink:
   name: str
   ingredients: dict[str, int]

@dataclass
class Resources:
    limits: dict[str, int]

class ProductionModel:
    def __init__(self, drinks: list[Drink], resources: Resources):
        self.model = LpProblem("Production", LpMaximize)
        self.vars = {drink.name: LpVariable(drink.name, lowBound=0, cat="Integer") for drink in drinks}
        self.model += sum(self.vars.values())


    def solve(self):
        self.model.solve()
        return {k: v.value() for k, v in self.vars.items()}