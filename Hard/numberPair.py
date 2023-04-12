"""Create a function that determines how many number pairs are there embedded in a space-separated string. The first numeric value in the 
space-separated string represents the count of the numbers, thus, excluded in the pairings.
Examples

number_pairs("7 1 2 1 2 1 3 2") ➞ 2
# (1, 1), (2, 2)

number_pairs("9 10 20 20 10 10 30 50 10 20") ➞ 3
# (10, 10), (20, 20), (10, 10)

number_pairs("4 2 3 4 1") ➞ 0
# although two 4's are present but
# the first one is discounted

Notes

Always take into consideration the first number in the string is not part of the pairing, thus, the count. It may not seem so useful as 
most people see it, but it's mathematically significant if you deal with set operations."""

def number_pairs(txt):
    txt = list(map(int, txt.split()))
    pairsDict = {v:txt.count(v) // 2 for v in txt[1:]}

    tupleLst = []
    for i in txt[1:]:
        if i == txt[0]:
            continue
        if pairsDict[i] != 0:
            tupleLst.append((i,i)) 
            pairsDict[i] -=1
    return tupleLst
    return", ".join(list(map(str,tupleLst)))

print(number_pairs("7 1 2 1 2 1 3 2")) # ➞ 2  (1, 1), (2, 2)))
print(number_pairs("9 10 20 20 10 10 30 50 10 20")) # ➞ 3  (10, 10), (20, 20), (10, 10)))
print(number_pairs("4 2 3 4 1")) # ➞ 0# although two 4's are present but

str_vectors = ["7 1 2 1 2 1 3 2", "9 10 20 20 10 10 30 50 10 20", "4 2 3 4 1",
               "13 10 20 20 10 10 30 50 10 20 50 50 30 20", "10 1 2 5 6 5 2 1 7 8 1",
               "16 2 3 5 11 1 11 5 7 9 13 17 3 8 7 2 1", "6 1 2 2 4 3 4"]

for i in str_vectors:
    print(number_pairs(i))


#create a set of txt use dictionary comprehension to create pairs. So key ==  number(from set) and pairs from txt which is split
# iterate through each element in txt
# create blank variable for tuples list
# 2 For i in text[1:] if i == txt[0] ignore
# 3 if statement if i dictionary val != 0. tuples list append (i,i). dictionary value -= 1
# 4 else continue
# 5 return tuple list
# 4 Divide count of li

def number_pairs(txt):
	lst = txt.split()[1:]
	return sum(lst.count(i)//2 for i in set(lst))
