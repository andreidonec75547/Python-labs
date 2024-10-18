
# Контрольная работа 1, Лабораторная работа 2, задание 2 уровня, номер 1

sumin = 0
rost = list(map(int, input().split()))

for num in rost:
    sumin += num

col = len(rost)
print(sumin/col)
