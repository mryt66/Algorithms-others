def czy_pusta(tablica):
    if not tablica:
        return True
    return False

def sort(tablica,el,prior):
    for i in range(len(tablica)-1):
        if tablica[i+1][1]<=tablica[i][1]:
            tmp=tablica[i]
            tablica[i]=tablica[i+1]
            tablica[i+1]=tmp
    return tablica

def usun(tablica): # usuwanie z konca
    x=slice(0,len(tablica)-1)
    return tablica[x]

def dodaj(tablica,el,prior,max): #dodawanie na koniec
    if czy_pusta==True:
        tablica[0]=[0,0]
        tablica[0]=[el, prior]
    if len(tablica) >= max:
        tablica=usun(tablica)
        tablica+=[[el,prior]]
    else:
        tablica += [[el, prior]]
    sort(tablica,el,prior)
    return tablica

max=5
Kolejka=[[5,1],[6,2],[7,3],[8,4]] # cyfra po przecinku-priorytet(im większa tym wyższy priorytet)
print(Kolejka)
Kolejka=dodaj(Kolejka,5,3,max)
print(Kolejka)
