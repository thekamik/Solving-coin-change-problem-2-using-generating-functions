from sympy import symbols, expand, Poly, Pow
import math
from itertools import count
from functools import reduce


# Define the global variable, that represent symbol
x = symbols('x')

def lcm(a, b):
    # calculate least common multiple
    return abs(a * b) // math.gcd(a, b)

def create_series(step, limit):
    # Buffer to store terms
    terms = []

    # Find all terms
    for i in count():
        power = i*step
        terms.append(Pow(x, power))

        # If it was last element, then finish execution
        if power == limit:
            break

    # Return series
    return sum(terms)


def find_value(amount, numbers):
    
    # Find common denominator
    common_denominator = reduce(lcm, numbers)

    # Define the series that represent our coins. Each series should contain powers less than the common denominator 
    series = []
    for num in numbers:
        series.append(create_series(num, common_denominator-num))

    # Multiply the series
    result = (reduce(lambda a, b: expand(a * b), series))

    # Extract coefficients and reverse the order
    coefficients = Poly(result, x).coeffs()[::-1]

    # find the remainder of the division and the number of whole parts
    r = amount % common_denominator
    q = (int)((amount - r) / common_denominator)
    
    # Max number of coefficients
    coeff_num = len(numbers) - 1

    # Calculate values
    calc = 0
    for i in range(coeff_num):
        # Calculatie value
        pos = r + i*common_denominator

        # Only values lesser than amount should be added to solution
        if pos <= amount:
            calc += coefficients[r + i*common_denominator] * math.comb(q+(coeff_num-i), coeff_num)

    # Return solution
    return calc
    


if __name__ == "__main__":

    # Define amount
    amount = 5000

    # Define coins
    numbers = [1,2,3,5]

    # Calculate number of exchanges
    solution = find_value(amount, numbers)

    # Display solution
    print(f"solution: {solution}")



    # solution: 696738362

