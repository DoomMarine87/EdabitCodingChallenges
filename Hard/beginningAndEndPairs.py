"""Write a function that print(pairs the first number in an array with the last, the second number with the second to last, etc.
Examples

pairs([1, 2, 3, 4, 5, 6, 7]) ➞ [[1, 7], [2, 6], [3, 5], [4, 4]]

pairs([1, 2, 3, 4, 5, 6]) ➞ [[1, 6], [2, 5], [3, 4]]

pairs([5, 9, 8, 1, 2]) ➞ [[5, 2], [9, 1], [8, 8]]

pairs([]) ➞ []

Notes

    If the list has an odd length, repeat the middle element twice for the last pair.
    Return an empty list if the input is an empty list."""

def pairs(lst):
    return list(map(list,(zip(lst[:len(lst)//2+1 if len(lst)%2 else len(lst)//2],lst[::-1]))))

print(pairs([1, 2, 3, 4, 5, 6, 7])) # ➞ [[1, 7], [2, 6], [3, 5], [4, 4]]
print(pairs([1, 2, 3, 4, 5, 6])) # ➞ [[1, 6], [2, 5], [3, 4]]
print(pairs([5, 9, 8, 1, 2])) # ➞ [[5, 2], [9, 1], [8, 8]]
print(pairs([])) # ➞ []

"""pairs=lambda lst:[[num,lst.pop()]for num in lst]"""
"""pairs=lambda l:[[l[x],l[-(x+1)]]for x in range((len(l)+1)//2)]"""
"""def pairs(lst):
    return [[lst[i],lst[-i-1]] for i in range((len(lst)+1)//2)]"""
"""def pairs(lst):
	return [[a,b] for a,b in zip(lst,lst[::-1])][:(len(lst)+1)//2]"""
