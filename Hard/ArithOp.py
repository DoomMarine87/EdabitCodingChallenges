"""Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

For example:

"15 // 0"  ➞ -1

Examples

arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1"""

def arithmetic_operation(n):
    a, op, b = n.split()

    if op == "+":
        return int(a) + int(b)
    if op == "-":
        return int(a) - int(b)
    if op == "*":
        return int(a) * int(b)
    if b == 0:
        return -1
    return int(a) // int(b)

print(arithmetic_operation("12 + 12"))

"""def arithmetic_operation(equation):
    '''
    Returns the result of evaluating the string equation
    '''
    from operator import add, sub, floordiv, mul

    OPS = {'+':add, '-':sub, '*':mul, '//':floordiv}
    a,op,b = equation.split()
    
    try:
        return OPS[op](int(a),int(b)) 
    except ZeroDivisionError:
        return -1"""

"""OP = {'+':int.__add__, '-':int.__sub__, '*':int.__mul__,
      '//': lambda a,b: a//b if b else -1 }

def arithmetic_operation(n):
    a, o, b = n.split()
    return OP[o](int(a), int(b))"""

