"""Create a function that will take a HEX number and returns the binary equivalent (as a string).
Examples

to_decimal(0xFF) ➞ "11111111"

to_decimal(0xAA) ➞ "10101010"

to_decimal(0xFA) ➞ "11111010"

Notes

The number will be always an 8-bit number."""

def to_decimal(num):
    hexToDec = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6,
                "7" : 7, "8": 8, "9": 9, "A" : 10, "B" : 11, "C": 12, "D": 13,
                "E" : 14, "F": 15 }

    num = list(num[-2:])
    
    dec = (hexToDec[num[0]] * 16)  + (hexToDec[num[1]] * 1)
    
    return dec


print(to_decimal("0xFF"))
print(to_decimal("0xAA"))
print(to_decimal("0xFA"))




