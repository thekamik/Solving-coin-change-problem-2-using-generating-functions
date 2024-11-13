# Solving the Coin Change Problem 2 Using Generating Functions

This repository contains a Python solution to the "Coin Change 2" problem, where the objective is to determine the number of ways to make change for a given amount using specific coin denominations.

The solution is designed to be flexible, allowing it to compute the number of ways to make change for any target amount, not just the specified 5000 PLN. By utilizing generating functions, the solution can easily adapt to different target values and coin denominations.

## Exercise
> In how many ways can 5000 PLN be exchanged using coins of 1, 2, 3, and 5 PLN denominations?

## Key Features
- **Generality**: Solves the coin change problem for any input amount, using any specified set of coin denominations.
- **Efficient Computation**: Uses generating functions to effectively calculate the number of ways to make change.

## Libraries Used
- **SymPy**: For symbolic mathematics, polynomial expansion, and simplification.
- **itertools**: For iteration utilities.
- **functools**: For functional programming utilities.
