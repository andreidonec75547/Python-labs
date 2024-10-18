Vector = [1, 2, 3, 4, 5]
Vector2 = []
sumin = 0

for x in Vector:
    Vector2.append(x**2)

for num in Vector2:
    sumin += num
print(sumin ** 0.5)
