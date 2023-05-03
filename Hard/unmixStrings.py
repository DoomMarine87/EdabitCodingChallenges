"""lPaeesh le pemu mnxit ehess rtnisg! Oh, sorry, that was supposed to say: Please help me unmix these strings!

Somehow my strings have all become mixed up; every pair of characters has been swapped. Help me undo this so I can understand my strings again.
Examples

unmix("123456") ➞ "214365"

unmix("hTsii  s aimex dpus rtni.g") ➞ "This is a mixed up string."

unmix("badce") ➞ "abcde"

Notes

The length of a string can be odd — in this case the last character is not altered (as there's nothing to swap it with)."""

def unmix(txt):
    if len(txt)%2:
        return "".join(j for i in zip(txt[1::2],txt[::2]) for j in i)+txt[-1]
    return "".join(j for i in zip(txt[1::2],txt[::2]) for j in i)
    
    
print(unmix("123456")) # ➞ "214365"
print(unmix("hTsii  s aimex dpus rtni.g")) # ➞ "This is a mixed up string."
print(unmix("badce")) # ➞ "abcde"

"""def unmix(txt):
	return ''.join(txt[i:i+2][::-1] for i in range(0,len(txt),2))"""

"""from itertools import zip_longest

def unmix(txt):
	return ''.join(a+b for a, b in zip_longest(txt[1::2], txt[::2], fillvalue=''))"""