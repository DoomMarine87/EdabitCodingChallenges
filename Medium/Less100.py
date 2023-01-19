"""Given two numbers, return True if the sum of both numbers is less than 100. Otherwise return False.
Examples

less_than_100(22, 15) ➞ True
# 22 + 15 = 37

less_than_100(83, 34) ➞ False
# 83 + 34 = 117

less_than_100(3, 77) ➞ True"""

def less_than_100(a, b):
    return a + b < 100

print(less_than_100(22, 15))
print(less_than_100(83, 34))
print(less_than_100(3, 77))