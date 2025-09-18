p = 23
g = 5
a = 11  # segreto di Alice

# pubblico di Alice
A = pow(g, a, p)
print("A =", A)  # dovrebbe dare 22

# pubblico di Bob (dato)
B = 16

# chiave segreta condivisa
KA = pow(B, a, p)  # Alice calcola
print("KA =", KA)

# ora scopriamo b sapendo che B = g^b mod p
for b in range(1, p):
    if pow(g, b, p) == B:
        print("b =", b)
        KB = pow(A, b, p)
        print("KB =", KB)
