"""In cricket, an over consists of six deliveries a bowler bowls from one end. Create a function that takes the number of balls bowled by a bowler and calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls.
Examples

total_overs(2400) ➞ 400

total_overs(164) ➞ 27.2
# 27 overs and 2 balls were bowled by the bowler.

total_overs(945) ➞ 157.3
# 157 overs and 3 balls were bowled by the bowler.

total_overs(5) ➞ 0.5"""

def total_overs(balls):

    previous6Div = 0
    for i in range(balls - 6, balls):
        if i % 6 == 0:
            previous6Div += i
    
    return balls // 6 if balls % 6 == 0 else float(str(balls // 6) + "." + str(balls - previous6Div))

print(total_overs(2400))
print(total_overs(164))
print(total_overs(945))

"""def total_overs(balls):
  return balls//6 + balls%6/10"""

print(164//6)
print(164%6)