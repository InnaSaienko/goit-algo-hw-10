# Monte Carlo Integration

## Task Description
This project demonstrates how to compute a definite integral using the Monte Carlo method and verify the result using an exact numerical method.

The function `f(x) = x²` is integrated over the interval `[0, 2]`.

---

## Methods Used

### Monte Carlo Method
The Monte Carlo method estimates the integral by:
- generating many random values of `x` in the interval `[a, b]`
- computing the average value of `f(x)`
- multiplying the average by `(b - a)`

The accuracy improves as the number of random samples increases.

### Exact Integration
To verify the Monte Carlo result, the integral is also computed using the `quad` function from `scipy.integrate`, which provides a highly accurate numerical solution.

---

## Verification
The Monte Carlo result is compared with the exact value obtained by `quad`.
This comparison confirms the correctness and accuracy of the Monte Carlo method.

---

## Conclusion
- The Monte Carlo method provides an approximate solution.
- Increasing the number of samples improves accuracy.
- The `quad` method serves as a reference for validation.
- Monte Carlo is useful when analytical solutions are difficult or impossible.
