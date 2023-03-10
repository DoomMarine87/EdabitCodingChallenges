"""Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"

Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"
"""

def encrypt(word):
    
    vowels = {"a" : 0, "e" : 1, "i" : 2, "o" : 2, "u" : 3}

    for c in word:
        if c in vowels:
            word = word.replace(c, str(vowels[c]))
    
    return word[::-1] + "aca"

print(encrypt("apple"))

"""def encrypt(word):
    v= {'a':'0','e':'1','o':'2','u':'3'}
    return ''.join(v[i] if i in v else i for i in word[::-1]) +'aca'

print(encrypt("apple"))"""

"""def encrypt(word):
	return word[::-1].translate(str.maketrans('aeou', '0123')) + 'aca'"""


