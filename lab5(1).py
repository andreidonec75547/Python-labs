#Лабораторная работа 5, задание 1 уровня, номер 2
#Два треугольника заданы длинами своих сторон а, b и с. Определить треугольник с большей площадью, вычисляя площади треугольников по формуле Герона
#S=√p(p-a)(p-b)(р-с),
#где р=(a+b+c)/2.

trk1 = list(map(int, input("Введите длину каждой стороны(a,b,c) первого треугольника: ").split()))
trk2 = list(map(int, input("Введите длину каждой стороны(a,b,c) второго треугольника: ").split()))

mrt = []

def yravnen(p, a, b, c):
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def pppppp(a, b, c):
    return (a + b + c) / 2

for i in trk1:
    mrt.append(i)

a1 = mrt[0]
b1 = mrt[1]
c1 = mrt[2]

p1 = pppppp(a1, b1, c1)

S1 = round(yravnen(p1, a1, b1, c1))

mrt.clear()
for n in trk2:
    mrt.append(n)

a2 = mrt[0]
b2 = mrt[1]
c2 = mrt[2]

p2 = pppppp(a2, b2, c2)

S2 = round(yravnen(p2, a2, b2, c2))

print('Площадь первого треугольника:',S1, 'Площадь второго треугольника: ',S2)

try:
    if S1 > S2:
        print(S1)
    else:
        print(S2)
except (TypeError, ZeroDivisionError):
    print('Невозможно вычеслить, треугольника не сушествует')
    
