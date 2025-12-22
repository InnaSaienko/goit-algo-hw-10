from dataclasses import dataclass

from pulp import LpProblem, LpMaximize, LpVariable, PULP_CBC_CMD


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

        for resource, limit in resources.limits.items():
            self.model += sum(drink.ingredients.get(resource, 0) * self.vars[drink.name] for drink in
                              drinks) <= limit  # the sum of all resources for all drinks must not exceed the available quantity

    def solve(self):
        solver = PULP_CBC_CMD(msg=False) # tells CBD don't print anything.
        self.model.solve(solver)
        result = {k: v.value() for k, v in self.vars.items()}
        print(f'\n"\033[1mOptimal production:\033[0m"', result)