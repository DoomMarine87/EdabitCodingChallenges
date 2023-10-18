# Function to perform the majority operation(a,b,c)
a = "01101010000010011110011001100111"
b = "10111011011001111010111010000101"
c = "00111100011011101111001101110010"

def maj(a,b,c):
    return "".join(["0" if sum([int(a[i]),int(b[i]),int(c[i])]) <= 1 else "1" for i in range(32)])

print(maj(a,b,c))
