#bubble sort
dane=[1,3.5,4,2,8,123,23,9]
for i in range(len(dane)):
    for j in range(1,len(dane)):
        if dane[j]<dane[j-1]:
            tmp=dane[j]
            dane[j]=dane[j-1]
            dane[j-1]=tmp
print(dane)
