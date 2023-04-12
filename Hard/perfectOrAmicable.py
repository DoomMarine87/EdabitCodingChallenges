"""Given a positive number x, if all the positive divisors of x (excluding x) add up to x, then x is said to be a perfect number.

For example, the set of positive divisors of 6 excluding 6 itself is (1, 2, 3). The sum of this set is 6. Therefore, 6 is a perfect number.

Given a positive number x, if all the positive divisors of x add up to a second number y, and all the positive divisors of y add up to x, 
then x and y are said to be a pair of amicable numbers.

Create a function that takes a number and returns "Perfect" if the number is perfect, "Amicable" if the number is part of an amicable pair, 
or "Neither".
Examples

num_type(6) ➞ "Perfect"

num_type(2924) ➞ "Amicable"

num_type(5010) ➞ "Neither"""

"""def num_type(n):
    sumN = sum(i for i in range(1, n//2+1)if not n%i)
    sumX = sum(i for i in range(1, sumN//2+1) if not sumN%i)
    return"Perfect" if sumN==n else "Amicable" if sum(i for i in range(1, sumX//2+1) if not sumX%i)==sumN else "Neither"

print(num_type(6))
print(num_type(2924))
print(num_type(5010))"""

def num_type(n):
    sumX = sum(i for i in range(1, n//2+1) if not n%i)
    return "Perfect" if sumX==n else "Amicable" if sum(i for i in range(1, sumX//2+1) if not sumX%i)==n else "Neither"

print(num_type(6))
print(num_type(2924))
print(num_type(5010))

"""def num_type(n):
	s = sum(factors(n))
	return 'Perfect' if s==n else 'Amicable' if sum(factors(s))==n else 'Neither'

def factors(n):
	return [i for i in range(1, (n//2) + 1) if not n%i]"""

"""def num_type(n):
	s = sum([i for i in range(1,n) if n%i == 0])
	if s == n:
		return 'Perfect'
	s1 = sum([i for i in range(1,s) if s%i == 0])
	if s1 == n:
		return 'Amicable'
	return 'Neither'"""
