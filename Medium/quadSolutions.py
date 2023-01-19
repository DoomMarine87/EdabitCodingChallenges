"""A quadratic equation a x² + b x + c = 0 has either 0, 1, or 2 distinct solutions for real values of x. Given a, b and c, you 
should return the number of solutions to the equation.
Examples

solutions(1, 0, -1) ➞ 2
// x² - 1 = 0 has two solutions (x = 1 and x = -1).

solutions(1, 0, 0) ➞ 1
// x² = 0 has one solution (x = 0).

solutions(1, 0, 1) ➞ 0
// x² + 1 = 0 has no real solutions."""

def solutions(a, b, c):
    
    res = (b ** 2) - (4 * a * c)

    if res > 0:
        return 2
    elif res == 0:
        return 1
    else:
        return 0

print(solutions(1, 0, -1))
print(solutions(1, 0, 0))
print(solutions(1, 0, 1))

"""def solutions(a, b, c):
    return 2 if (b ** 2) - (4 * a * c) > 0 else 1 if (b ** 2) - (4 * a * c) == 0 else 0   

print(solutions(1, 0, -1))
print(solutions(1, 0, 0))
print(solutions(1, 0, 1))"""

"""def solutions(a, b, c):
    res = (b ** 2) - (4 * a * c)

    return 2 if res > 0 else 1 if res == 0 else 0

print(solutions(1, 0, -1))
print(solutions(1, 0, 0))
print(solutions(1, 0, 1))"""
