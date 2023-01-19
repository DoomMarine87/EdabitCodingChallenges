"""Write a function that takes a list of numbers and returns a list with two elements:

    The first element should be the sum of all even numbers in the list.
    The second element should be the sum of all odd numbers in the list.

Example

sum_odd_and_even([1, 2, 3, 4, 5, 6]) ➞ [12, 9]
# 2 + 4 + 6 = 12 and 1 + 3 + 5 = 9

sum_odd_and_even([-1, -2, -3, -4, -5, -6]) ➞ [-12, -9])

sum_odd_and_even([0, 0]) ➞ [0, 0])"""

def sum_odd_and_even(lst):
    return [sum(i for i in lst if i % 2 == 0), sum(i for i in lst if i % 2 != 0)]

print(sum_odd_and_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_and_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_and_even([0, 0]))

"""def sum_odd_and_even(lst):
	return [sum(e for e in lst if e%2==i) for i in [0,1]]"""

"""def sum_odd_and_even(lst):
	return [sum(i for i in lst if not i%2), sum(i for i in lst if i%2)]"""