from monte_carlo_worker import monte_carlo_worker
from exact_integral_by_quad import exact_integral
from visualizing_result import visualizing_result


def integration_function(x):
    """Target integration function"""

    return x ** 2



def main() -> None:
    """Run Monte Carlo integration"""

    a, b = 0, 2
    number_of_points = 100000

    result_monte_carlo = monte_carlo_worker(integration_function, a, b, number_of_points)
    result_quad = exact_integral(integration_function, a, b)

    print("Monte Carlo integration: ", result_monte_carlo)
    print("Exact:", result_quad)
    print(f"Absolute deviation: {abs(result_monte_carlo - result_quad)}")

    visualizing_result(integration_function, a, b, number_of_points)


if __name__ == "__main__":
    main()
