"""Given an integer, create a function that returns the next prime. If the number is prime, return the number itself.
Examples

next_prime(12) ➞ 13

next_prime(24) ➞ 29

next_prime(11) ➞ 11
# 11 is a prime, so we return the number itself."""

def next_prime(num):
    flag = False
    for i in range(num, num + num // 2 + 1):
        if i == 1:
            return 2
        if i <= 3:
            return i
        if not i%2 or not i%3:
            flag = True
        for j in range(5, i // 2 + 1, 2):
            if not i % j:
                flag = True
                break
        if not flag:
            return i
        flag = False       

print(next_prime(12)) # ➞ 13
print(next_prime(24)) # ➞ 29
print(next_prime(11)) # ➞ 11
print(next_prime(13)) # 13)
print(next_prime(14)) # 17)
print(next_prime(33)) #, 37)
print(next_prime(1))

"""def next_prime(num):
	while [i for i in range(2, num // 2 + 1) if num%i==0]:
		num+=1
	return num


print(next_prime(12)) # ➞ 13
print(next_prime(24)) # ➞ 29
print(next_prime(11)) # ➞ 11
print(next_prime(13)) # 13)
print(next_prime(14)) # 17)
print(next_prime(33)) #, 37)
print(next_prime(1))"""

