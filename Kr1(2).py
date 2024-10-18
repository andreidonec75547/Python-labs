sumin = 0
rost = list(map(int, input().split()))

for num in rost:
    sumin += num

col = len(rost)
print(sumin/col)
