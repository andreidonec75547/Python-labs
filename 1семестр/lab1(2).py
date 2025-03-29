
#Лабораторная работа 1, задание 2 уровня, номер 2 

numms = [ ]
i = 1
roton = 1

while i < 30:
    numms.append(i)
    i += 3

while roton < 30000:
    for num in numms:
        roton *= num
        if roton > 30000:
            print(num-3)
            break
