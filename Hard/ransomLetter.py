"""Write a function that returns True if you can use the letters of the first string to create the second string. Letters are case 
sensitive.

Examples

can_build("aPPleAL", "PAL")) # ➞ True

can_build("aPPleAL", "apple")) # ➞ False

can_build("a", "")) # ➞ True

can_build("aa", "aaa")) # ➞ False

Notes

Letters in the first string can be used only once."""

def can_build(s1, s2):
   return "".join([i for i in s2 if s2.count(i) <= s1.count(i)]) == s2

print(can_build("aPPleAL", "PAL")) #➞ True
print(can_build("aPPleAL", "apple")) # ➞ False
print(can_build("a", "")) # ➞ True
print(can_build("aa", "aaa")) # ➞ False"""

print(can_build("aPPleAL", "PAL")) #, True)
print(can_build("OAT", "OAT")) #, True)
print(can_build("maybelLINE", "maybe")) #, True)
print(can_build("topsh", "shop")) #, True)
print(can_build("topshSHP", "SHoP")) #, True)
print(can_build("DAISIES", "SAID")) #, True)
print(can_build("ToporP", "porT")) #, True)
print(can_build("PoTluCK", "PuCK")) #, True)
print(can_build("pATS", "p")) #, True)
print(can_build("blah", "")) #, True)
print(can_build("aPPleAL", "apple")) #, False)
print(can_build("shortCAKE", "cakey")) #, False)
print(can_build("maybeLINE", "lINE")) #, False)
print(can_build("teaPOT", "lINE")) #, False)
print(can_build("", "a")) #, False)
print(can_build("a", "aA")) #, False)
print(can_build("a", "A")) #, False)
print(can_build("AAAAAA", "AAAAAAa")) #, False)
print(can_build("apple", "appleY")) #, False)
print(can_build("xxYYzZ", "zzZxYxY")) #, False)
print(can_build("abCD", "aBCD")) #, False)

"""def can_build(s1, s2):
	return all(s2.count(i) <= s1.count(i) for i in s2)"""