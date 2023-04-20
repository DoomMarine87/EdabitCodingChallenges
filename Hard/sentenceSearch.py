"""Create a function that returns the whole of the first sentence which contains a specific word. Include the full stop at the 
end of the sentence.

Examples

txt = "I have a cat. I have a mat. Things are going swell."

sentence_searcher(txt, "have") ➞ "I have a cat."

sentence_searcher(txt, "MAT") ➞ "I have a mat."

sentence_searcher(txt, "things") ➞ "Things are going swell."

sentence_searcher(txt, "flat") ➞ ""

Notes

    Sentences will always end with a period.
    Your function should not be case sensitive.
    Return an empty string if the word isn't found in the sentence."""

import re
txt = "I have a cat. I have a mat. Things are going swell."
def sentence_searcher(txt, word):
    match = [i.strip() + "." for i in txt.split(".") if re.search(word, i, re.IGNORECASE)]
    return "" if len(match) == 0 else match[0]

print(sentence_searcher(txt, "have")) # ➞ "I have a cat."
print(sentence_searcher(txt, "MAT")) # ➞ "I have a mat."
print(sentence_searcher(txt, "things")) # ➞ "Things are going swell."
print(sentence_searcher(txt, "flat")) # ➞ ""

def sentence_searcher(txt, word):
    match = list(filter(lambda x: word.lower() in x ,txt.lower().split(".")))
    return "" if len(match) == 0 else match[0].strip().capitalize() + "."

print(sentence_searcher(txt, "have")) # ➞ "I have a cat."
print(sentence_searcher(txt, "MAT")) # ➞ "I have a mat."
print(sentence_searcher(txt, "things")) # ➞ "Things are going swell."
print(sentence_searcher(txt, "flat")) # ➞ ""

"""def sentence_searcher(txt, word):
	txt = txt.split('.')
	for i in txt:
		if word.lower() in i.lower():
			return i.strip()+'.'
	return ''"""

