#Лабораторная работа 8, номер 12
#12. Считая, что в памяти компьютера хранится таблица кодов ча- сто встречающихся слов, ввести текст в массив, заменяя слова кода- ми после ввода. Распечатать текст в исходном виде, т.е. заменяя коды словами.

slovo = {
    'd': 7,
    'f': 0,
    'g': 2
}

text = 'dfgdfgfddfgfffdfggdgfgggdfd'
for kei in slovo.keys():
    text = text.replace(kei, str(slovo[kei]))
print(text)
