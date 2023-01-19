"""Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the 
vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.
Example

uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"

uncensor("abcd", "") ➞ "abcd"

uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

Notes

    The vowels are given in the correct order.
    The number of vowels will match the number of * characters in the censored string."""

def uncensor(txt, vowels):
    newTxt = ""
    vowels = list(vowels)
    for l in txt:
        if l != "*":
            newTxt += l
        else:
            newTxt += vowels[0]
            del vowels[0]
            
    return newTxt

print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(uncensor("abcd", ""))
print(uncensor("*PP*RC*S*", "UEAE"))

"""def uncensor(txt, vowels):
	txt = txt.replace('*', '{}')
	return txt.format(*vowels)"""

"""def uncensor(txt, vowels):
	vowels = iter(vowels)
	return ''.join(next(vowels) if i == '*' else i for i in txt)"""

"""def uncensor(t, v):
	for c in v: t = t.replace('*', c, 1)
	return t"""

"""uncensor=lambda t,v:t.replace('*','{}').format(*v)"""





