from production import Drink, Resources, ProductionModel


def main() -> None:
    drinks = [
        Drink("Lemonade", {"Water": 2, "Sugar": 1, "Lemon": 1}),
        Drink("Juice", {"Water": 1, "Puree": 2}),
    ]

    resources = Resources(
        {"Water": 100, "Sugar": 50, "Lemon": 30, "Puree": 40}
    )

    ProductionModel(drinks, resources).solve()



if __name__ == "__main__":
    main()
