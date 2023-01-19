"""Create a function that finds the highest integer in the list using recursion.
Examples

find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

find_highest([0, 12, 4, 87]) ➞ 87

find_highest([8]) ➞ 8"""

def find_highest(lst):
    highest = -999999999999

    for i in lst:
        if i > highest:
            highest = i
    return highest

print(find_highest([-1, 3, 5, 6, 99, 12, 2]))
print(find_highest([0, 12, 4, 87]))
print(find_highest([8]))




