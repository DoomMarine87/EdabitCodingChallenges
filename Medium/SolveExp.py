"""Create a function that takes a number a and finds the missing exponent x so that a when raised to the power of x is equal to b.
Examples

solve_for_exp(4, 1024) ➞ 5

solve_for_exp(2, 1024) ➞ 10

solve_for_exp(9, 3486784401) ➞ 10"""

import math

def solve_for_exp(a, b):
    return round(math.log(b, a), 2)

print(solve_for_exp(4, 1024))
print(solve_for_exp(2, 1024))
print(solve_for_exp(9, 3486784401))
