import array
import codecs
#import numpy as np

#
# Try to extract the plaintext from this word encoded using Autokey. We do not know the key k
# FTPNIH
# Brute forcing (there are only 26 characters)
#

#print("b".encode(encoding="ascii")[0])

def transformStringToInter(texts):
    numbers = []
    i = 0
    for c in texts:
        numbers.append(c.encode(encoding="ascii")[0] - "a".encode(encoding="ascii")[0])
    return numbers

def transformIntegerToString(numbers):
    texts = []
    i = 0
    for i in numbers:
        texts.append(codecs.decode(int.to_bytes("a".encode(encoding="ascii")[0] + i), encoding="ascii"))
    return texts

CIPHERTEXT = "FTPNIH"

cprTxt = transformStringToInter(CIPHERTEXT.lower())
print(cprTxt)
for k in range(1, 27):
    #keyInt = "a".encode(encoding="ascii")[0] + k
    #keyChr = codecs.decode(int.to_bytes(keyInt), encoding="ascii")
    result = []
    y = cprTxt[0]
    x = (y - k) % 26
    result.append(x)
    for y in cprTxt[1:]:
        x = (y - x) % 26
        result.append(x)
    print(k, transformIntegerToString(result))
        



### y_i = z_i + x_i mod 26 
### for z_1 = k, z_i = x_i-1
# 5  = k  + x1
# 19 = x1 + x2
# 15 = x2 + x3
# 13 = x3 + x4
# 8  = x4 + x5
# 7  = x5 + x6
