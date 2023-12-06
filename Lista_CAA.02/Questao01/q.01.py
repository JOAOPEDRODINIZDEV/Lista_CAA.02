def decompor_vetor(S, piv, p, r):
    q1 = p - 1   
    q2 = r + 1  
    i = p

    while i < q2:
        if S[i] < piv:
            q1 += 1
            S[i], S[q1] = S[q1], S[i]
            i += 1
        elif S[i] == piv:
            i += 1
        else:
            q2 -= 1
            S[i], S[q2] = S[q2], S[i]

    return q1, q2

S = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
p = 2
r = 9
piv = S[p]  
q1, q2 = decompor_vetor(S, piv, p, r)

print("Vetor rearranjado:", S)
print("q1:", q1)
print("q2:", q2)
