"""Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.
Examples

print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) # ➞ 17

print(sum_primes([2, 3, 4, 11, 20, 50, 71]) # ➞ 87

print(sum_primes([]) # ➞ None

Notes

    Given numbers won't exceed 101.
    A prime number is a number which has exactly two divisors."""

def sum_primes(lst):
    return sum([i for i in lst if 2 in(i, 2**i%i)]) if len(lst) >= 1 else None # or None

print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # ➞ 17
print(sum_primes([2, 3, 4, 11, 20, 50, 71])) # ➞ 87
print(sum_primes([])) # ➞ None

"""def sum_primes(lst):
	isprime = lambda n: n>1 and all(n % i for i in range(2, int(n**0.5)+1))
	return sum(n for n in lst if isprime(n)) or None"""