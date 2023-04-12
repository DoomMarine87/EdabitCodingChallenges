"""Given a word, create a function which returns whether or not it's possible to create a palindrome by rearranging the letters in the word.
Examples

is_palindrome_possible("rearcac") ➞ True
# You can make "racecar"

is_palindrome_possible("suhbeusheff") ➞ True
# You can make "sfuehbheufs" (not a real word but still a palindrome)

is_palindrome_possible("palindrome") ➞ False
# It's impossible

Notes

    Trivially, words which are already palindromes return True.
    Words are given in all lowercase."""

def is_palindrome_possible(txt):
    return sum(txt.count(l) for l in txt) >= len(txt)*2-1

print(is_palindrome_possible("rearcac")) #, True)
print(is_palindrome_possible("suhbeusheff")) #, True)
print(is_palindrome_possible("palindrome")) #, False)
print(is_palindrome_possible("yagnx")) #, False)
print(is_palindrome_possible("zgzqxljjp")) #, False)
print(is_palindrome_possible("tgmqkpdhnhatoco")) #, False)
print(is_palindrome_possible("akyka")) #, True)
print(is_palindrome_possible("kjyyrftnbsbq")) #, False)
print(is_palindrome_possible("jynmynqhcy")) #, False)
print(is_palindrome_possible("hfe")) #, False)
print(is_palindrome_possible("noon")) #, True)
print(is_palindrome_possible("azmkallbanpu")) #, False)
print(is_palindrome_possible("drrede")) #, True)
print(is_palindrome_possible("xmhwcocldjdnqvv")) #, False)
print(is_palindrome_possible("reparpe")) #, True)
print(is_palindrome_possible("jnavz")) #, False)
print(is_palindrome_possible("orort")) #, True)
print(is_palindrome_possible("mel")) #, False)
print(is_palindrome_possible("jdxknf")) #, False)
print(is_palindrome_possible("qo")) #, False)
print(is_palindrome_possible("neett")) #, True)
print(is_palindrome_possible("wow")) #, True)
print(is_palindrome_possible("avkkiaapiusuapspiip")) #, True)
print(is_palindrome_possible("aann")) #, True)
print(is_palindrome_possible("iivcc")) #, True)
print(is_palindrome_possible("akyka")) #, True)
print(is_palindrome_possible("eelvl")) #, True)
print(is_palindrome_possible("damam")) #, True)
print(is_palindrome_possible("mmo")) #, True)
print(is_palindrome_possible("ge")) #, False)
print(is_palindrome_possible("arrad")) #, True)
print(is_palindrome_possible("bq")) #, False)
print(is_palindrome_possible("djufyllynldw")) #, False)
print(is_palindrome_possible("reparpe")) #, True)
print(is_palindrome_possible("ttraoor")) #, True)
print(is_palindrome_possible("orort")) #, True)
print(is_palindrome_possible("asgas")) #, True)
print(is_palindrome_possible("t")) #, True)
print(is_palindrome_possible("tstsa")) #, True)
print(is_palindrome_possible("neett")) #, True)
print(is_palindrome_possible("wndnwrkpkihup")) #, False)

"""def is_palindrome_possible(txt):
	return sum(txt.count(i)%2 for i in set(txt)) <= 1"""
