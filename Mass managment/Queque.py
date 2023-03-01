def czy_pusta(tablica):
    if len(tablica)==0:
        return True
    return False
def odczytpoczatku(tablica):
    return (len(tablica)-1)
def usun(tablica): #usuwanie z poczatku
    x=slice(1,len(tablica))
    return tablica[x]
def dodaj(tablica,el,max): #dodawanie na koniec
    if len(tablica)>=max: #jeżeli kolejka jest pełna to wtedy usuwa 1szy element i dodaje ostatni na koniec
        x=slice(1,len(tablica))
        tablica=tablica[x]
    y=tablica+[el]
    return y
l=[1,2,3]
l=dodaj(l,5,4)
print(l)
l=usun(l)
print(l)