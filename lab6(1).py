#Лабораторная работа 6, задание 1 уровня, номер 3

class test:
    name = None
    col = None

    def uno_test(self, name, col):
        self.name = name
        self.col = col

k1 = test()
k1.uno_test("Эйнштейн", 52)

k2 = test()
k2.uno_test("Бор", 35)

k3= test()
k3.uno_test("Планк", 37)

k4 = test()
k4.uno_test("Рик", 83)

k5 = test()
k5.uno_test("Зорич", 29)

k6 = test()
k6.uno_test("Тесла", 2)

k7 = test()
k7.uno_test("Ампер", 41)

k8 = test()
k8.uno_test("Ренген", 42)

k9 = test()
k9.uno_test("Резерфорд", 16)

k10 = test()
k10.uno_test("неизвестный", 22)

golos = [k1.col, k2.col, k3.col, k4.col, k5.col, k6.col, k7.col, k8.col, k9.col, k10.col]
golos.sort(reverse=True)
print(golos)

dop = [k1.col, k2.col, k3.col, k4.col, k5.col, k6.col, k7.col, k8.col, k9.col, k10.col]
name = [k1.name, k2.name, k3.name, k4.name, k5.name, k6.name, k7.name, k8.name, k9.name, k10.name]

totol = 0

for num in dop:
     totol += num

for g in golos:
    if g >= golos[4]:
        for prov in dop:
            if prov == g:
                i = dop.index(prov)
                print(name[i], "процент голосов:", round(dop[i] / totol * 100), "%")
              
