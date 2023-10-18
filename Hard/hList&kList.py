def primes(n):
    p = []
    c = 2

    while len(p) < n:
        flag = True

        for i in range(2, (c//2) + 1):
            if not c%i:
                flag = False
                break
            
        if flag:
            p.append(c)
        c += 1
    return p

def hexToBin(hex):
    hexBinDict = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", 
                  "8":"1000", "9":"1001", "a":"1010", "b":"1011", "c":"1100", "d":"1101", "e":"1110", "f":"1111"}
    
    return "".join([hexBinDict[i] for i in hex])

hList = [float(i ** 0.5).hex().split(".")[1][:8] for i in primes(8)]

# hList = "".join([hexToBin(j) for i in hList for j in i])

# hList2 = ""
# for i in range(len(hList)):
#         if not i % 32 and i != 0:
#             hList2 += ","
#         hList2 += hList[i]

# print(list(map(lambda x: len(x),hList2)))

# print(hList)


print(primes(20))


