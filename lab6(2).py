# Лабораторная работа 6, задание 2 уровня, номер 1

class exam:
    name = None
    exam1 = None
    exam2 = None
    exam3 = None
    exam4 = None

    def norm(self, name, exam1, exam2, exam3, exam4):
        self.name = name
        self.exam1 = exam1
        self.exam2 = exam2
        self.exam3 = exam3
        self.exam4 = exam4

def forc(sr):
    total = 0
    for i in sr:
        total += i
    return (total / 4)

y1 = exam()
y1.norm("Рик", 3, 3, 4, 5)
sr1 = [y1.exam1, y1.exam2, y1.exam3, y1.exam4]
n1 = forc(sr1)

y2 = exam()
y2.norm("Эйнштейн", 4, 3, 4, 5)
sr2 = [y2.exam1, y2.exam2, y2.exam3, y2.exam4]
n2 = forc(sr2)

y3 = exam()
y3.norm("Морти", 3, 2, 3, 2)
sr3 = [y3.exam1, y3.exam2, y3.exam3, y3.exam4]
n3 = forc(sr3)

y4 = exam()
y4.norm("Планк", 5, 5, 5, 5)
sr4 = [y4.exam1, y4.exam2, y4.exam3, y4.exam4]
n4 = forc(sr4)

y5 = exam()
y5.norm("Фародей", 4, 3, 4, 4)
sr5 = [y5.exam1, y5.exam2, y5.exam3, y5.exam4]
n5 = forc(sr5)

y6 = exam()
y6.norm("Ломоносов", 2, 3, 4, 5)
sr6 = [y6.exam1, y6.exam2, y6.exam3, y6.exam4]
n6 = forc(sr6)

y7 = exam()
y7.norm("Роберт", 3, 3, 3, 3)
sr7 = [y7.exam1, y7.exam2, y7.exam3, y7.exam4]
n7 = forc(sr7)

y8 = exam()
y8.norm("Норман", 5, 3, 4, 5)
sr8 = [y8.exam1, y8.exam2, y8.exam3, y8.exam4]
n8 = forc(sr8)

vse = [n1, n2, n3, n4, n5, n6, n7, n8]
name = [y1.name, y2.name, y3.name, y4.name, y5.name, y6.name, y7.name, y8.name]

kol = []

for a in vse:
    if a >= 4:
        kol.append(a)

roc = kol.sort(reverse=True)

print("Результаты по среднему балу за 4 ээкзамена, учитывая толь тех чей средний бал не меньше 4:")
for n in kol:
    for g in vse:
        if n == g:
            i = vse.index(n)
            print(name[i], n)
