def quicksort(array):
    less = []
    equal = []
    more = []
    if len(array) > 1:
        co = array[0]
        for x in array:
            if x < co:
                less.append(x)
            elif x == co:
                equal.append(x)
            elif x > co:
                more.append(x)
        return quicksort(less)+equal+quicksort(more)
    else:
        return array
l1=[2,3,1,7657,123,1556]
l1=quicksort(l1)
print(l1)