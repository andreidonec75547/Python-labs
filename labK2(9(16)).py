
file = open('dan.py', 'w')

file.write('4 5 8 12 1 3 2')

file.close()


pon = open('dan.py', 'r')

lol = (pon.read())
word_l = lol.split()

num = []
for word in word_l:
    if word.isnumeric():
        num.append(int(word))

n = 0
for i in num:
    n += i

l = len(num)

f = n / l

kon = []
for a in num:
    if a < f:
        p = num.index(a)
        kon.append(p)

print(kon)

pon.close()
