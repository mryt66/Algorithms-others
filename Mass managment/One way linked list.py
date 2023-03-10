#lista jednokierunkowa
class listaJednokierukowa():
    def __init__(self):
        self.head = None
        self.dl = 0

    def dodaj(self, element, indeks):
        if indeks > self.dl or indeks < 0:
            print("Nie mozna dodac elementu o tym indeksie")
        else:
            if indeks == 0:
                element.next = self.head
                self.head = element
            else:
                sprawdzany = self.head
                for i in range(indeks):
                    sprawdzany = sprawdzany.next
                element.next = sprawdzany
                sprawdzany = self.head
                for i in range(indeks - 1):
                    sprawdzany = sprawdzany.next
                sprawdzany.next = element
            self.dl += 1
            print("Dodano " + str(element.value))

    def usun(self, indeks):
        if indeks > self.dl - 1 or indeks < 0:
            print("Nie można usunąć elementu o podanym indeksie")
            return ""
        if indeks == 0:
            usuwany = self.head
            self.head = self.head.next
        else:
            pop = self.head
            for i in range(indeks - 1):
                pop = pop.next
            usuwany = pop.next
            pop.next = pop.next.next
        self.dl -= 1
        print("Usunięto " + str(usuwany.value))

    def pokazListe(self):
        if self.head == None:
            print("Brak elementow")
        else:
            print("\nLista el: ")
            sprawdzany = self.head
            while sprawdzany != None:
                print(sprawdzany.value)
                sprawdzany = sprawdzany.next

    def szukaj(self, value):
        sprawdzany = self.head
        while sprawdzany != None:
            if sprawdzany.value == value:
                print("Taki element jest w liście")
                return ""
            else:
                sprawdzany = sprawdzany.next
        print("Nie ma takiego elementu w liście")


class elements():
    def __init__(self, value):
        self.next = None
        self.value = value


lista1 = listaJednokierukowa()
lista1.pokazListe()
el1 = elements(1)
el2 = elements(2)
el3 = elements(3)
el4 = elements(4)
el5 = elements(5)
lista1.pokazListe()
lista1.dodaj(el1, 0)
lista1.pokazListe()
lista1.dodaj(el2, 1)
lista1.dodaj(el3, 2)
lista1.dodaj(el4, 3)
lista1.pokazListe()
lista1.szukaj(5)
lista1.szukaj(1)
lista1.pokazListe()
lista1.usun(3)
lista1.usun(0)
lista1.pokazListe()



