class MList:
    def __init__(self, capacity):
        self._capacity = capacity
        self.mlist = list()
        if self._capacity < 0:
            raise ValueError("Lista nie może mieć ujemnej pojemność")

    def pojemnosc(self):
        return self._capacity

    def rozmiar(self):
        return len(self.mlist)

    def pisz(self):
        print("Rozmiar listy:", self.rozmiar())
        print("Pojemnosc listy:", self._capacity)
        print("Elementy ", self.mlist)

    def dodaj_element(self, element):
        if self._capacity == self.rozmiar():
            return False
        self.mlist.append(element)
        return True

    def znajdz(self, szukana):
        num = 0
        while num < len(self.mlist):
            if self.mlist[num] == szukana:
                return num
            num += 1
        return -1

    def pobierz(self, indeks):
        if len(self.mlist) <= indeks or indeks < 0:
            raise IndexError("Odwolanie do nieistniejacego elementu")
        return self.mlist[indeks]

    def usun_powtorzenia(self, val):
        lock = False

        nowalista = list()

        for x in self.mlist:
            if val == x and lock is True:
                continue
            elif val == x:
                lock = True
            nowalista.append(x)

        self.mlist = nowalista

    def odwroc(self):
        self.mlist.reverse()

    def zwieksz_pojemnosc(self, val):
        if val < 0:
            return False
        self._capacity += val
        return True

    def zmniejsz_pojemnosc(self, val):
        if val < 0 or (self.pojemnosc()-val) < self.rozmiar():
            return False
        self._capacity -= val
        return True
