
slovo = {
    'd': 7,
    'f': 0,
    'g': 2
}

text = 'dfgdfgfddfgfffdfggdgfgggdfd'
for kei in slovo.keys():
    text = text.replace(kei, str(slovo[kei]))
print(text)
