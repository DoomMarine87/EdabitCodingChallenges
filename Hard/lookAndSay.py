"""Given an integer, return a new integer according to the rules below:

    Split the number into groups of two digit numbers. If the number has an odd number of digits, return "invalid".
    For each group of two digit numbers, concatenate the last digit to a new string the same number of times as the value of the 
    first digit.
    Return the result as an integer.

print(look_and_say(3132) ➞ 111222

# By reading the number digit by digit, you get three "1" and three "2".
# Therefore, you put three ones and three two's together.
# Remember to return an integer.

Examples

print(look_and_say(95) ➞ 555555555

print(look_and_say(1213141516171819) ➞ 23456789

print(look_and_say(120520) ➞ 200

print(look_and_say(231) ➞ "invalid"

Notes

    Note that the number 0 can be included (see example #3).
    Check the Resources tab for a TED-Ed video for extra clarity."""

def look_and_say(n):
    n = str(n)
    return int("".join(int(n[i]) * n[i+1] for i in range(0,len(n), 2))) if not len(n)%2 else "invalid"

print(look_and_say(95)) # ➞ 555555555
print(look_and_say(1213141516171819)) # ➞ 23456789
print(look_and_say(120520)) # ➞ 200
print(look_and_say(231)) # ➞ "invalid"""   

"""def look_and_say(n):
	n = str(n)
	if len(n)%2:
		return 'invalid'
	return int(''.join(int(n[i]) * n[i+1] for i in range(0, len(n), 2)))"""

"""def look_and_say(n):
    s = str(n)
    if len(s)%2:
        return 'invalid'
    return int(''.join(b*int(a) for a, b in zip(s[::2], s[1::2])))"""
