"""Write a function that returns True if a given name can generate an array of words.
Examples

anagram("Justin Bieber", ["injures", "ebb", "it"]) ➞ True

anagram("Natalie Portman", ["ornamental", "pita"]) ➞ True

anagram("Chris Pratt", ["chirps", "rat"]) ➞ False
# Not all letters are used

anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) ➞ False
# "s" does not exist in the original name

Notes

    Each letter in the name may only be used once.
    All letters in the name must be used."""

def anagram(name, words):
    return sorted("".join(name.split()).lower()) == sorted("".join(words))


"""print(anagram("Justin Bieber", ["injures", "ebb", "it"])) # ➞ True
print(anagram("Natalie Portman", ["ornamental", "pita"])) # ➞ True
print(anagram("Chris Pratt", ["chirps", "rat"])) # ➞ False
# Not all letters are used
print(anagram("Jeff Goldblum", ["jog", "meld", "bluffs"])) # ➞ False
# "s" does not exist in the original name"""

print(anagram("Justin Bieber", ["injures", "ebb", "it"])) #, True)
print(anagram("Natalie Portman", ["ornamental", "pita"])) #, True)
print(anagram("Emma Watson", ["mows", "meant", "a"])) #, True)
print(anagram("Daniel Radcliffe", ["clarified", "elf", "and"])) #, True)
print(anagram("Tom Hiddleston", ["tenths", "mood", "lid"])) #, True)
print(anagram("Blake Lively", ["key", "veal", "bill"])) #, True)
print(anagram("Ryan Reynolds", ["yonder", "sly", "ran"])) #, True)
print(anagram("Kristen Stewart", ["trinkets", "war", "set"])) #, True)
print(anagram("Chris Pratt", ["chirps", "rat"])) #, False)
print(anagram("Jeff Goldblum", ["jog", "meld", "bluffs"])) #, False)
print(anagram("Taylor Swift", ["stratify", "ow"])) #, False)
print(anagram("Adam Levine", ["medieval", "man"])) #, False)
print(anagram("Blake Shelton", ["betoken", "all", "she"])) #, False)
print(anagram("Miley Cyrus", ["lyric", "my", "suer"])) #, False)
print(anagram("Matt Damon", ["madman"])) #, False)
print(anagram("Graham Norton", ["graham", "not", "or"])) #, False)

"""def anagram(name, words):
	return sorted(''.join(words) + ' ') == sorted(name.lower())"""

"""def anagram(name, words):
	return sorted(name.lower().replace(" ", "")) == sorted("".join(words))"""