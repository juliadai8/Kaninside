def max_permutations(M):
    l = set(M)
    for i in range(len(M)):
        indeks = M[i]
        while indeks != i:
            indeks = M[indeks]
            if indeks == i:
                l.remove(M[indeks])
                l.remove(M[i])
                break
    return l

print('h')
liste = [1,2,3,4,4]
print(max_permutations(liste))
liste = [0]
print(max_permutations(liste))