


import random
Mol = [random.randint(-(10**10), 10**10) for _ in range(8)]
print(Mol)

kol = list(filter(lambda x: x > 0, Mol))
long = max(kol)
ind = Mol.index(long)
Mol[ind+1] *= 2
print(Mol)
