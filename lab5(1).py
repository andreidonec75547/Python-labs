trk1 = list(map(int, input("Введите длину каждой стороны(a,b,c) первого треугольника: ").split()))
trk2 = list(map(int, input("Введите длину каждой стороны(a,b,c) второго треугольника: ").split()))

mrt = []

for i in trk1:
    mrt.append(i)

a1 = mrt[0]
b1 = mrt[1]
c1 = mrt[2]

p1 = (a1 + b1 + c1) / 2

S1 = (p1 * (p1 - a1) * (p1 - b1) * (p1 - c1)) ** 0.5

mrt.clear()
for n in trk2:
    mrt.append(n)

a2 = mrt[0]
b2 = mrt[1]
c2 = mrt[2]

p2 = (a2 + b2 + c2) / 2

S2 = (p2 * (p2 - a2) * (p2 - b2) * (p2 - c2)) ** 0.5

print('Площадь первого треугольника:',S1, 'Площадь второго треугольника: ',S2)

if S1 > S2:
    print(S1)
else:
    print(S2)
