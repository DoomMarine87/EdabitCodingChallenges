"""Create a function that counts the number of blocks of two or more adjacent 1s in a list.
Examples

count_ones([1, 0, 0, 1, 1, 0, 1, 1, 1])) # ➞ 2
# Two instances: [1, 1] (middle)) # and [1, 1, 1] (end)) #

count_ones([1, 0, 1, 0, 1, 0, 1, 0])) # ➞ 0

count_ones([1, 1, 1, 1, 0, 0, 0, 0])) # ➞ 1

count_ones([0, 0, 0])) # ➞ 0

Notes

    A single 1 by itself (surrounded by a zero on its left and right)) #, does not count towards the total (see first example)) #.
    Each input will contain only zeroes and ones."""
import re
def count_ones(lst):
    return len(re.findall('1{2,}', "".join(map(str,lst))))

print(count_ones([1, 0, 0, 1, 1, 0, 1, 1, 1])) # ➞ 2
# Two instances: [1, 1] (middle)) # and [1, 1, 1] (end)) #
print(count_ones([1, 0, 1, 0, 1, 0, 1, 0])) # ➞ 0
print(count_ones([1, 1, 1, 1, 0, 0, 0, 0])) # ➞ 1
print(count_ones([0, 0, 0])) # ➞ 0

"""def count_ones(lst):
	return str(lst+[0]).count('1, 1, 0')"""

"""def count_ones(lst):
  return("".join(str(i) for i in lst)+"0").count("110")"""

"""count_ones=lambda l:sum(len(e)>5for e in str(l).split("0"))"""

"""count_ones=lambda A:('0'+''.join(map(str,A))).count('011')"""