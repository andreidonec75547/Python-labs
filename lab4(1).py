matr = [[8, 9, 3, 1, 6], [-6, -45, 7, 2, 21], [56, 83, -25, -89, 54], [90, 37, -15, 32, 72], [-10, -40, 72, 71, -86], [3, 8, 75, 14, 9]]

def negativFunc(matr, r, c):
    coun = 0
    for i in range(r):
        for j in range(c):
            if matr[i][j] < 0:
                coun += 1
    return coun
    
print(negativFunc)
