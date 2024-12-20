matr = [[92, 25, 19, 55, 8, 35, 12], [89, 34, 45, 48, 42, 55, 18], [11, 79, 56, 42, 16, 23, 76], [46, 31, 1, 65, 37, 39, 16], [13, 17, 95, 51, 37, 92, 59]]

total = 0
for num in matr:
    for matr_num in num:
        total += matr_num

print(total)
