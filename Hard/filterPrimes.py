"""Create a function that takes a list and returns a new list containing only prime numbers.
Examples

filter_primes([7, 9, 3, 9, 10, 11, 27]) ➞ [7, 3, 11]

filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70]) ➞ [10007, 1009]

filter_primesfilter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097]) ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]"""

def filter_primes(num):
    numPrimes = []
    flag = False
    for i in num:
        if i <= 1:
            continue
        if i <= 3:
            numPrimes.append(i)
        if not i%2 or not i%3:
            continue
        for j in range(5, i // 2  + 1, 2):
            if not i%j:
                flag = True
                break
        if not flag:
            numPrimes.append(i)
        flag = False
    return numPrimes



print(filter_primes([7, 9, 3, 9, 10, 11, 27])) # ➞ [7, 3, 11]
print(filter_primes([10007, 1009, 1007, 27, 147, 77, 1001, 70])) # ➞ [10007, 1009]
print(filter_primes([1009, 10, 10, 10, 3, 33, 9, 4, 1, 61, 63, 69, 1087, 1091, 1093, 1097])) # ➞ [1009, 3, 61, 1087, 1091, 1093, 1097]
print(filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])) #, [2, 3, 5, 7, 11, 13, 17, 19, 23])

"""filter_primes = lambda a: [x for x in a if 2 in [x, 2**x%x]]"""

"""def filter_primes(num):
	return [i for i in num if 2 in (i, 2**i%i)]"""

"""For any unaware, I've seen Frank Huff and Deep Xavier use this, amazing-to-me... if 2 in [num, 2**num%num] for Primes, 
saving an additional def...

num =  1      2**num =  2      2**num%num =  0
num =  2      2**num =  4      2**num%num =  0
num =  3      2**num =  8      2**num%num =  2<<<
num =  4      2**num =  16      2**num%num =  0
num =  5      2**num =  32      2**num%num =  2<<<
num =  6      2**num =  64      2**num%num =  4
num =  7      2**num =  128      2**num%num =  2<<<
num =  8      2**num =  256      2**num%num =  0
num =  9      2**num =  512      2**num%num =  8
num =  10      2**num =  1024      2**num%num =  4
num =  11      2**num =  2048      2**num%num =  2<<<

Can, of course, shorten to if 2 in [n,2**n%n]"""

