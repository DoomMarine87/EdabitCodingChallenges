"""Write a function that takes coordinates of two points on a two-dimensional plane and returns the length of the line segment connecting those two points.
Examples

line_length([15, 7], [22, 11]) ➞ 8.06

line_length([0, 0], [0, 0]) ➞ 0

line_length([0, 0], [1, 1]) ➞ 1.41"""

def line_length(dot1, dot2):
    return round((((dot2[0] - dot1[0]) **2 + (dot2[1] - dot1[1]) **2) ** 0.5), 2) 

print(line_length([15, 7], [22, 11]))
print(line_length([0, 0], [0, 0]))
print(line_length([0, 0], [1, 1]))



