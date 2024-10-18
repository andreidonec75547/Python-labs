
# Контрольная работа 1, Лабораторная работа 1, задание 1 уровня, номер 8
# Вычислить s = 1! + 2! + ... + 6!

spot = [1, 2, 3, 4, 5, 6]
goh = []
sumin = 0

for num in spot:
    factorial = 1

    while num > 1:
        factorial = factorial * num
        num = num - 1

    goh.append(factorial)

for col in goh:
    sumin += col
    
print(sumin)



# Контрольная работа 1, Лабораторная работа 1, задание 2 уровня, номер 5
a = 13
i = a
b = 7
h = -1
while a > 0:
    a -= b
    h += 1
print(h)
print(i - b*h)
