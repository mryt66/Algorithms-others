class listaDwukierunkowa():
    def __init__(self):
        self.head = None
        self.tail = None
        self.dl = 0

    def dodaj(self, element, indeks):
        if indeks > self.dl or indeks < 0:
            print("Nie można dodać elementu o tym indeksie")
            return ""
        sprawdzany = self.head
        if sprawdzany == None:
            self.head = element
            self.tail = element
        else:
            for i in range(indeks):
                sprawdzany = sprawdzany.next
            if sprawdzany == None:
                element.previous = self.tail
                self.tail.next = element
                self.tail = element
            elif sprawdzany.previous != None:
                sprawdzany.previous.next = element
                element.previous = sprawdzany.previous
                element.next = sprawdzany
                sprawdzany.previous = element
            else:
                element.next = self.head
                self.head = element
                sprawdzany.previous = element
        self.dl += 1
        print("Dodano " + str(element.value))

    def usun(self, indeks):
        if indeks > self.dl - 1 or indeks < 0:
            print("Nie można usunać elementu o tym indeksie")
            return ""
        sprawdzany = self.head
        for i in range(indeks):
            sprawdzany = sprawdzany.next
        if sprawdzany.next != None:
            if sprawdzany.previous != None:
                sprawdzany.previous.next = sprawdzany.next
            else:
                self.head = sprawdzany.next
            sprawdzany.next.previous = sprawdzany.previous
        else:
            if sprawdzany.previous != None:
                sprawdzany.previous.next = sprawdzany.next
            else:
                self.head = None
            self.tail = sprawdzany.previous
        self.dl -= 1

    def pokazListe(self):
        if self.head == None:
            print("Brak elementów")
            return ""
        sprawdzany = self.head
        print("\nLista: ")
        while sprawdzany != None:
            print(sprawdzany.value)
            sprawdzany = sprawdzany.next

    def pokazListeOdOgona(self):
        if self.tail == None:
            print("Brak elementów")
            return ""
        sprawdzany = self.tail
        print("\nLista od tyłu: ")
        while sprawdzany != None:
            print(sprawdzany.value)
            sprawdzany = sprawdzany.previous

    def szukaj(self, value):
        sprawdzany = self.head
        while sprawdzany != None:
            if sprawdzany.value == value:
                print("Jest taki element w liście")
                return 0
            else:
                sprawdzany = sprawdzany.next
        print("Nie ma takiego el w liscie")


class elementy():
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value


lista1 = listaDwukierunkowa()
lista1.pokazListe()
el1 = elementy(1)
el2 = elementy(2)
el3 = elementy(3)
el4 = elementy(4)
lista1.pokazListe()
lista1.dodaj(el1, 0)
lista1.dodaj(el2, 1)
lista1.dodaj(el3, 2)
lista1.pokazListe()
lista1.dodaj(el4, 3)
lista1.pokazListe()
lista1.szukaj(5)
lista1.szukaj(1)
lista1.usun(3)
lista1.usun(0)
lista1.pokazListe()
lista1.pokazListeOdOgona()