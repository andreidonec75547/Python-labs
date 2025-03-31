#Лабораторная работа 8, номер 12
#12. Считая, что в памяти компьютера хранится таблица кодов часто встречающихся слов, ввести текст в массив, заменяя слова кодами после ввода. Распечатать текст в исходном виде, т.е. заменяя коды словами.

#создаем словарь для хранения кодов слов
word_codes = {
    "привет": 1,
    "мир": 2,
    "как": 3,
    "дела": 4,
    "спасибо": 5,
    "пожалуйста": 6,
    "пока": 7,
    "хорошо": 8,
    "плохо": 9,
    "нормально": 10,
    "и": 11,
    "а": 12
}

#создаем обратный словарь для декодирования
code_words = {v: k for k, v in word_codes.items()}


#функция для кодирования текста
def encode_text(text):
    words = text.split()
    encoded_text = []

    for word in words:
        #убираем знаки припенания
        clean_word = word.strip(".,!?;:()[]{}")

        #заменям слово из словаря кодом
        if clean_word.lower() in word_codes:
            encoded_text.append(str(word_codes[clean_word.lower()]))
        else:
            encoded_text.append(word)

    return encoded_text


#функция для декодирования текста
def decode_text(encoded_text):
    decoded_text = []

    for item in encoded_text:
        #заменяем код словом
        if item.isdigit():
            decoded_text.append(code_words.get(int(item), item))
        else:
            decoded_text.append(item)

    return " ".join(decoded_text)


#ввод текста
input_text = [input("Введите текст: ")]

for intext in input_text:
    #кодирование
    encoded = encode_text(intext)
    print("\nЗакодированный текст:")
    print(encoded)



#декодирование
decoded = decode_text(encoded)
print("\nДекодированный текст:")
print(decoded)
