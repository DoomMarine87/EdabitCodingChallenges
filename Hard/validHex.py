"""Create a function that determines whether a string is a valid hex code.

A hex code must begin with a pound key # and is exactly 6 characters in length. Each character must be a digit from 0-9 or an alphabetic 
character from A-F. All alphabetic characters may be uppercase or lowercase.
Examples

print(is_valid_hex_code("#CD5C5C") ➞ True

print(is_valid_hex_code("#EAECEE") ➞ True

print(is_valid_hex_code("#eaecee") ➞ True

print(is_valid_hex_code("#CD5C58C") ➞ False
# Length exceeds 6

print(is_valid_hex_code("#CD5C5Z") ➞ False
# Not all alphabetic characters in A-F

print(is_valid_hex_code("#CD5C&C") ➞ False
# Contains unacceptable character

print(is_valid_hex_code("CD5C5C") ➞ False
# Missing #"""

import re
def is_valid_hex_code(txt):
    return bool(re.match(r'#[\da-fA-F]{6}$', txt))

print(is_valid_hex_code("#CD5C5C")) # ➞ True
print(is_valid_hex_code("#EAECEE")) # ➞ True
print(is_valid_hex_code("#eaecee")) # ➞ True
print(is_valid_hex_code("#CD5C58C")) # ➞ False
# Length exceeds 6
print(is_valid_hex_code("#CD5C5Z")) # ➞ False
# Not all alphabetic characters in A-F
print(is_valid_hex_code("#CD5C&C")) # ➞ False
# Contains unacceptable character
print(is_valid_hex_code("CD5C5C")) # ➞ False
# Missing #"""

"""import re
is_valid_hex_code=lambda t:bool(re.match("^#[\da-fA-F]{6}$",t))"""