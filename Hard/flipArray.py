"""Create a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list.

In other words, take an 1 x n list (1 row + n columns) and flip it into a n x 1 list (n rows and 1 column), and vice versa.
Examples

flip_list([1, 2, 3, 4]) ➞ [[1], [2], [3], [4]]
# Take a horizontal list and flip it vertical.

flip_list([[5], [6], [9]]) ➞ [5, 6, 9]
# Take a vertical list and flip it horizontal.

flip_list([]) ➞ []

Notes

If given an empty list [], return an empty list []."""

def flip_list(lst):
    return lst if len(lst)==0 else[[i] for i in lst] if type(lst[0])==int else [j for i in lst for j in i]



print(flip_list([1,2,3,4]))
print(flip_list([[5],[6],[9]]))
print(flip_list([]))

"""def flip_list(lst):
    return [[i] if type(i) == int else i[0] for i in lst]"""

"""flip_list = lambda x: [i[0] if isinstance(i,list) else [i] for i in x]"""