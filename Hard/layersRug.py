"""Write a function that counts how many concentric layers a rug has.
Examples

count_layers([
  "AAAA",
  "ABBA",
  "AAAA"
]) ➞ 2

count_layers([
  "AAAAAAAAA",
  "ABBBBBBBA",
  "ABBAAABBA",
  "ABBBBBBBA",
  "AAAAAAAAA"
]) ➞ 3

count_layers([
  "AAAAAAAAAAA",
  "AABBBBBBBAA",
  "AABCCCCCBAA",
  "AABCAAACBAA",
  "AABCADACBAA",
  "AABCAAACBAA",
  "AABCCCCCBAA",
  "AABBBBBBBAA",
  "AAAAAAAAAAA"
]) ➞ 5

Notes

    Multiple layers can share the same component so count them separately (example #2).
    Layers will be horizontally and vertically symmetric.
    There will be at least one layer for each rug."""

def count_layers(rug):
    return len(set(rug))

"""def count_layers(rug):
    return len({v:rug.count(v) for v in rug})"""

print(count_layers([
"AAA"])) #, 1)
print(count_layers([
"AAAA", 
"AAAA", 
"AAAA"])) #, 1)
print(count_layers([
"AAAA", 
"ABBA", 
"AAAA"])) #, 2)
print(count_layers([
"AAAAAAAAA", 
"ABBBBBBBA", 
"ABBBBBBBA", 
"ABBBBBBBA", 
"AAAAAAAAA"])) #, 2)
print(count_layers([
"AAAAAAAAA", 
"ABBBBBBBA", 
"ABBAAABBA", 
"ABBBBBBBA", 
"AAAAAAAAA"])) #, 3)
print(count_layers([
"AAAAAAAAA", 
"ABBBBBBBA", 
"ABCCCCCBA", 
"ABBBBBBBA", 
"AAAAAAAAA"])) #, 3)
print(count_layers([
"AAAAAAAAAAA", 
"AABBBBBBBAA",
"AABCCCCCBAA",
"AABCAAACBAA",
"AABCADACBAA", 
"AABCAAACBAA",
"AABCCCCCBAA",
"AABBBBBBBAA",
"AAAAAAAAAAA"])) #, 5)
print(count_layers([
"AAAAAAAAAAA", 
"AABBBBBBBAA",
"AABCCCCCBAA",
"AABCAAACBAA",
"AABCABACBAA", 
"AABCAAACBAA",
"AABCCCCCBAA",
"AABBBBBBBAA",
"AAAAAAAAAAA"])) #, 5)
print(count_layers([
"AAAAAAAAAAA", 
"AABBBBBBBAA",
"AABCCCCCBAA",
"AABCDDDCBAA",
"AABCDDDCBAA", 
"AABCDDDCBAA",
"AABCCCCCBAA",
"AABBBBBBBAA",
"AAAAAAAAAAA"])) #, 4)
print(count_layers([
"FFFFFFFFFFFFFFFFFFFFFFFFF",
"FFFFFFFFFFFFFFFFFFFFFFFFF",
"FFFFGGGGGGGGGGGGGGGGGFFFF",
"FFFFGGGAAAAAAAAAAAGGGFFFF", 
"FFFFGGGAABBBBBBBAAGGGFFFF",
"FFFFGGGAABCCCCCBAAGGGFFFF",
"FFFFGGGAABCDDDCBAAGGGFFFF",
"FFFFGGGAABCDDDCBAAGGGFFFF", 
"FFFFGGGAABCDDDCBAAGGGFFFF",
"FFFFGGGAABCCCCCBAAGGGFFFF",
"FFFFGGGAABBBBBBBAAGGGFFFF",
"FFFFGGGAAAAAAAAAAAGGGFFFF", 
"FFFFGGGGGGGGGGGGGGGGGFFFF", 
"FFFFFFFFFFFFFFFFFFFFFFFFF", 
"FFFFFFFFFFFFFFFFFFFFFFFFF"])) #, 6)

