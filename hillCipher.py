import numpy as np

#
# Hill cipher encryption and decryption
#

print("#First practice")

def findNumberGivingOffOne(determinant: int):
    for i in range(0, 25):
        if (determinant*i % 26) == 1: return i
        else: continue

plnTxt = np.array([1,3])
encKey = np.array([[1,2],
               [4,3]])
encTxt = np.dot(plnTxt, encKey)

# decTxt = np.mod(np.dot(encTxt, np.linalg.inv(encKey)), 26)
# Above the commented code is same as below 5-lines of code.
detOfKey = (encKey[0][0]*encKey[1][1] - encKey[0][1]*encKey[1][0]) % 26
encKeyTrs = np.array([[encKey[1][1], encKey[0][1]*-1],
                      [encKey[1][0]*-1, encKey[0][0]]])
detOfKeyInv = np.dot(findNumberGivingOffOne(detOfKey), encKeyTrs)
decTxt = np.mod(np.dot(encTxt, detOfKeyInv), 26)

print(encTxt)
print(decTxt)
print()


#
# Assume that the attacker has two plaintext and ciphertext messages
# Can he find the key K?
# => known plain-cipher
#

print("#Second practice")

p1 = np.array([5,9])
p2 = np.array([2,5])
c1 = np.array([19,4])
c2 = np.array([24,11])
m = 2

plnTxt = np.array([p1, p2])
crtTxt = np.array([c1, c2])

# Here, use extended euclidian algorith to get inverse of determinant (det^-1 = (det * a) mod 26).
det = p1[0]*p2[1] - p1[1]*p2[0] # np.linalg.det(plnTxt) # ad - bc
q = 0       # start with 0, and will contain the value of division without remainder
tmp = det   # start with determinant, and will contain the remainder of division
c = 26      # start with the modulus number, and will contain the value of d of the previous step.
d = tmp     # always become of tmp in the same step.

e = 1       # start from 1, it is the euclidian variable which will be the return value for a.
f = 0       # start from 0, it will contain another tmp value.
tmp = e - q*f
e = f
f = tmp

while d != 0:
    q = int(c / d)
    print(f"q = {q}", end =" ")

    tmp = c % d
    c = d
    d = tmp
    print(f"tmp = {tmp},", end =" ")
    print(f"c = {c},", end =" ")
    print(f"d = {d},", end =" ")

    tmp = e - q * f
    e = f
    f = tmp
    print(f"tmp = {tmp},", end =" ")
    print(f"e = {e},", end =" ")
    print(f"f = {f}")

a = e % 26
print(a)

plnInv = det * np.linalg.inv(plnTxt)    # inversing without multiplying det^-1
detInv = np.dot(a, plnInv)
recoveryFromCrtTxt = np.dot(detInv, crtTxt)

print(detInv)
print(np.mod(recoveryFromCrtTxt, 26))
print()
