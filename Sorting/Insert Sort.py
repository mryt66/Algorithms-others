def insertsort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and key<array[j]:
            array[j+1]=array[j]
            j=j-1
        array[j+1]=key
l1=[9,3,5,1,2]
insertsort(l1)
print(l1)