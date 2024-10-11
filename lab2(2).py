norma = int(input("norma="))
inputs = list(map(int, input().split()))
soda = 0
for i in inputs:
    if i >= norma:
        soda += 1

print(soda)
