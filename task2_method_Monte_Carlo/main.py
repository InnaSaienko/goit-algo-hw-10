from monte_carlo_worker import monte_carlo_worker
from visualizing_result import visualizing_result


def integration_function(x):
    """Target integration function"""

    return x ** 2



def main() -> None:
    """Run Monte Carlo integration"""

    a, b = 0, 2

    print(f"Monte Carlo integration: ", monte_carlo_worker(integration_function, a, b, ))
    visualizing_result(integration_function, a, b)


if __name__ == "__main__":
    main()
