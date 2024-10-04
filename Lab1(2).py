numms =[ ]
i = 1
roton = 0

while roton < 30000:
    for num in numms:
        roton *= num
    while i <= 30:
        numms.append(i)
        i += 3    
                
print(roton)
