"""Create a function that takes two number strings and returns their sum as a string.
Examples

add("111", "111") ➞ "222"

add("10", "80") ➞ "90"

add("", "20") ➞ "Invalid Operation"

Notes

If any input is "" or None, return "Invalid Operation"."""

def add(n1, n2):
    return str((int(n1)) + int(n2) if n1 != "" and n2 != "" and n1 != None and n2 != None else "Invalid Operation")

print(add("111", "111"))
print(add("10", "80"))
print(add("", "20"))

"""def add(n1, n2):
    try:
        return str(int(n1) + int(n2))
    except:
        return "Invalid Operation"

print(add("111", "111"))
print(add("10", "80"))
print(add("", "20"))
print(add(None, "20"))"""

"""def add(n1, n2):
	return str(int(n1)+int(n2)) if n1 and n2 else 'Invalid Operation'"""


