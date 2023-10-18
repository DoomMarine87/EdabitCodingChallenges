# Function to perform the choose operation for the Sha256 algorithm

e = "01010001000011100101001001111111"
f = "10011011000001010110100010001100"
g = "00011111100000111101100110101011"

def ch(e,f,g):
    chBin = "".join([g[i] if e[i] == "0" else f[i] for i in range(len(e))])
    return chBin

print(ch(e,f,g))